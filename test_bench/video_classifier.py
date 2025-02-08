from typing import List

import av
import numpy as np
import torch
from huggingface_hub import hf_hub_download
from transformers import AutoModel, AutoProcessor

from test_bench.base_model import BaseModelTest


class VideoClassifier(BaseModelTest):
    model_name = "video-classifier"
    model = "microsoft/xclip-base-patch32"

    def __init__(self, video_options: List[str]):
        super().__init__(model_name=self.model_name)
        self.video_options = video_options
        self.video = None

        self.model_pipeline = None
        self.processor = None

    def read_video_pyav(self, container, indices):
        frames = []
        container.seek(0)
        start_index = indices[0]
        end_index = indices[-1]
        for i, frame in enumerate(container.decode(video=0)):
            if i > end_index:
                break
            if i >= start_index and i in indices:
                frames.append(frame)
        return np.stack([x.to_ndarray(format="rgb24") for x in frames])

    def sample_frame_indices(self, clip_len, frame_sample_rate, seg_len):
        converted_len = int(clip_len * frame_sample_rate)
        end_idx = np.random.randint(converted_len, seg_len)
        start_idx = end_idx - converted_len
        indices = np.linspace(start_idx, end_idx, num=clip_len)
        indices = np.clip(indices, start_idx, end_idx - 1).astype(np.int64)
        return indices

    @BaseModelTest.timecheck
    def load_video(self):
        file_path = hf_hub_download(
            repo_id="nielsr/video-demo",
            filename="eating_spaghetti.mp4",
            repo_type="dataset",
        )
        container = av.open(file_path)
        indices = self.sample_frame_indices(
            clip_len=8, frame_sample_rate=1, seg_len=container.streams.video[0].frames
        )
        self.video = self.read_video_pyav(container, indices)

    @BaseModelTest.timecheck
    def load_pipeline(self):
        self.processor = AutoProcessor.from_pretrained(self.model)
        self.model_pipeline = AutoModel.from_pretrained(self.model)

    @BaseModelTest.timecheck
    def run(self):
        inputs = self.processor(
            text=self.video_options,
            videos=list(self.video),
            return_tensors="pt",
            padding=True,
        )
        with torch.no_grad():
            outputs = self.model_pipeline(**inputs)

        logits_per_video = outputs.logits_per_video
        probs = logits_per_video.softmax(dim=1)
        print(probs)


if __name__ == "__main__":
    video_options = ["Nuclear energy", "eating spaghetti", "eating salchipapa"]

    text_generator = VideoClassifier(video_options)
    text_generator.load_pipeline()
    text_generator.run()
    text_generator.report_execution_times()

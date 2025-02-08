from test_bench.base_model import BaseModelTest
from transformers import pipeline


class TextGenerator(BaseModelTest):
    model_name = "text-generation"
    model = "microsoft/phi-4"

    def __init__(self, user_message: str):
        super().__init__(model_name=self.model_name)
        self.user_message = user_message
        self.pipe = None

    @BaseModelTest.timecheck
    def load_pipeline(self):
        self.pipe = pipeline(self.model_name, model=self.model, trust_remote_code=True)

    @BaseModelTest.timecheck
    def run(self):
        messages = [
            {"role": "user", "content": self.user_message},
        ]
        return self.pipe(messages)


if __name__ == "__main__":
    user_message = "hey"

    text_generator = TextGenerator(user_message)
    text_generator.load_pipeline()
    text_generator.run()
    text_generator.report_execution_times()

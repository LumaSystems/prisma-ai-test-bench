from litellm import completion

from config import ENV_VARIABLES
from test_bench.base_model import BaseModelTest


class TextGenerator(BaseModelTest):
    model_name = "text-generation"

    def __init__(self, user_message: str, model: str = "deepseek-coder"):
        super().__init__(model_name=self.model_name)
        self.user_message = user_message
        self.model = model

    @BaseModelTest.timecheck
    def load_pipeline(self):
        pass

    @BaseModelTest.timecheck
    def inference(self):
        return completion(
            model=f"ollama/{self.model}",
            messages=[{"content": self.user_message, "role": "user"}],
            api_base=ENV_VARIABLES["API_BASE"],
        )

    def run(self):
        self.load_pipeline()
        print(self.inference().choices[0].message.content)


if __name__ == "__main__":
    user_message = "Generate code"
    model = "deepseek-coder"
    params = {"user_message": user_message, "model": model}

    text_generator = TextGenerator(**params)
    text_generator.run()
    text_generator.report_execution_times()

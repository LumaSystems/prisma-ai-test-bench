from litellm import completion

from config import ENV_VARIABLES
from test_bench.base_model import BaseModelTest


class TextGenerator(BaseModelTest):
    model_name = "text-generation"
    model = "deepseek-r1:1.5b"

    def __init__(self, user_message: str):
        super().__init__(model_name=self.model_name)
        self.user_message = user_message

    @BaseModelTest.timecheck
    def load_pipeline(self):
        pass

    @BaseModelTest.timecheck
    def run(self):
        return completion(
            model=f"ollama/{self.model}",
            messages=[{"content": self.user_message, "role": "user"}],
            api_base=f"http://localhost:{ENV_VARIABLES['LITE_LLM_SERVER_PORT']}",
        )


if __name__ == "__main__":
    user_message = "Generate code"

    text_generator = TextGenerator(user_message)
    text_generator.load_pipeline()
    text_generator.run()
    text_generator.report_execution_times()

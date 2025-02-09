from test_bench.text_generator import TextGenerator
from test_bench.video_classifier import VideoClassifier

# Asegurarse que los modelos de TextGenerator están disponibles en Ollama
test_bench_list = [
    {
        "model": TextGenerator,
        "properties": {
            "model": "deepseek-coder",
            "user_message": "Write a Python function that takes a list of numbers and returns a dictionary with the sum, average, and median of the numbers. Include proper error handling.",
        },
    },
    {
        "model": TextGenerator,
        "properties": {
            "model": "deepseek-r1:1.5b",
            "user_message": "Explain the difference between supervised, unsupervised, and reinforcement learning. Provide real-world examples for each.",
        },
    },
    {
        "model": TextGenerator,
        "properties": {
            "model": "deepseek-r1:1.5b",
            "user_message": "Escribe un relato corto de ciencia ficción futurista (200 palabras) sobre un mundo en el que la IA se ha convertido en el gobierno. Describe su impacto en los seres humanos.",
        },
    },
    {
        "model": VideoClassifier,
        "properties": {
            "video_options": ["Nuclear energy", "eating spaghetti", "eating salchipapa"]
        },
    },
]


if __name__ == "__main__":
    for test in test_bench_list:
        model = test["model"](**test["properties"])
        print(f"==== Running test for: {model.model_name} ====")
        model.run()
    model.report_execution_times()

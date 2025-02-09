# Prisma AI Test Bench

A self-hosted benchmarking system to test different LLM (Large Language Model) and multimodal implementations on edge computing hardware using Ollama and HuggingFace.

## 📌 Features
- Run multiple LLMs sequentially to compare performance.
- Uses Ollama for lightweight self-hosted inference.
- Supports custom prompts to evaluate model responses.
- Logs execution times and outputs for analysis.


## 🚀 Running Ollama

### 1️⃣ Start Ollama
```bash
docker-compose up -d ollama
```

This runs the Ollama LLM server in the background.

### 2️⃣ Verify Ollama is Running
Enter the Ollama container:

```bash
docker exec -it ollama_server sh
```

Install curl (if needed):
```bash
apt update && apt install -y curl
```

Check if Ollama is responsive:

```bash
curl -v http://localhost:11434/api/tags
```

✅ Expected Response:
```bash
{"models": []}
```

### 🧠 Installing & Managing Models
Current implementation of test bench uses `deepsee-coder` & `deepseek-r1:1.5b`
```bash
ollama pull deepseek-coder
```
```bash
ollama pull deepseek-r1:1.5b
```

Please pull the required models and modify the `test_bench_list` in `test_bench/run_test_bench.py` to add a new Ollama model.

[Optional] Verify models are downloaded
```bash
curl -v http://localhost:11434/api/tags
```



## 📝 Running the Test Bench
Once models are installed, run the AI Model Tester:
```bash
docker-compose up ai-model-tester --build
```


This will:

1. Load and initialize each model.
2. Run predefined test prompts.
3. Log inference times and outputs.


Example inference time output:
```bash
Class: TextGenerator, Method: load_pipeline, Time: 0.0000 seconds
Class: TextGenerator, Method: inference, Time: 10.0831 seconds
Class: TextGenerator, Method: load_pipeline, Time: 0.0000 seconds
Class: TextGenerator, Method: inference, Time: 12.8251 seconds
Class: TextGenerator, Method: load_pipeline, Time: 0.0000 seconds
Class: TextGenerator, Method: inference, Time: 8.4731 seconds
Class: VideoClassifier, Method: load_video, Time: 0.5707 seconds
Class: VideoClassifier, Method: load_pipeline, Time: 1.8529 seconds
Class: VideoClassifier, Method: inference, Time: 2.6363 seconds
```

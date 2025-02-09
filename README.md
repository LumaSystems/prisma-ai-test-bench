# prisma-aitest-bench
Prisma AI Test Bench




verify ollama is running

```bash
docker exec -it ollama_server sh
```

```bash
apt update && apt install -y curl
```

```bash
curl -v http://localhost:11434/api/tags
```

if no models returned, install them

```bash
ollama pull deepseek-coder
```

add them to the model list to test

ensure model is installes

```bash
curl -v http://localhost:11434/api/tags
```

run test-bench
```bash
docker-compose up ai-model-tester --build
```

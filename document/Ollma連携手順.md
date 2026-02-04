# docker-compose.yml作成

```yml
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama-container
    ports:
      - "11434:11434"
    volumes:
      - ollama-data:/root/.ollama
    restart: always

volumes:
  ollama-data:

```

# dockerを起動

- docker compose up -d

# 動作確認

- docker exec -it ollama-container bash
- ollama pull llama3

```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3",
    "prompt": "Dockerとは何ですか？"
  }'

```

- docker compose down -v


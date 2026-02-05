# docker-compose.yml作成

```yml
version: "3.9"

services:
  nginx:
    image: nginx:latest
    ports:
      - "8080:80"   # ホストの8080番でアクセス可能に
    volumes:
      - ./html:/usr/share/nginx/html:ro  # ホストのhtmlをコンテナにマウント
```

# dockerを起動

- docker compose up -d

# 動作確認

- http://localhost:8080


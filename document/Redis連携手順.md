# docker-compose.yml作成

```yml
version: '3.8'

services:
  redis:
    image: redis:7
    container_name: redis-container
    restart: always
    ports:
      - "6379:6379"

```

# dockerを起動

- docker compose up -d

# 動作確認

- docker exec -it redis-container redis-cli
- SET user:1 "test_data"
- GET user:1

- SET session:abc123 "test_TTL" EX 10
- TTL session:abc123
- GET session:abc123

- docker compose down
  * -vをつけなくてもキャッシュサーバなので再起動するとデータは削除される



# docker-compose.yml作成

```yml
version: '3.8'

services:
  rabbitmq:
    image: rabbitmq:3-management
    container_name: rabbitmq-container
    restart: always
    ports:
      - "5672:5672"     # AMQP（アプリ用）
      - "15672:15672"   # 管理画面
    environment:
      RABBITMQ_DEFAULT_USER: sample_user
      RABBITMQ_DEFAULT_PASS: sample_pass
```

# dockerを起動

- docker compose up -d

# 動作確認

- http://localhost:15672
    * 画面でadd Queueする
- docker exec -it rabbitmq-container bash
- rabbitmqctl list_queues

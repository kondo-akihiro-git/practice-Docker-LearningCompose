# docker-compose.yml作成

```yml
version: "3.9"

services:
  jenkins:
    image: jenkins/jenkins:lts
    user: root  # 権限問題を避ける
    ports:
      - "8080:8080"  # Jenkins Web UI
      - "50000:50000"  # エージェント接続用
    volumes:
      - jenkins_home:/var/jenkins_home

volumes:
  jenkins_home:

```

# dockerを起動

- docker compose up -d

# 動作確認

- docker compose logs -f jenkins
- http://localhost:8080



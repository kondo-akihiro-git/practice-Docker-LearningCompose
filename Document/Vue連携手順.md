# 一時的なDockerクライアントにログイン

- docker run -it --rm -u $(id -u):$(id -g) -v ${PWD}:/app -w /app node:20 bash

# Dockerクライアント内でプロジェクト作成

- npx @vue/cli@5 create . --default --no-git
- exit 

+ プロジェクト作成時点ではコンテナ内ユーザーにGitの書き込み権限がないので初期化スキップを追加しております。

# docker-compose.yml作成

```yml
version: '3.8'

services:
  vue:
    image: node:20
    container_name: vue-app
    working_dir: /app
    volumes:
      - ./:/app
    ports:
      - "8080:8080"
    command: >
      sh -c "npm install && npm run serve -- --host 0.0.0.0"
    user: "${UID}:${GID}"

```

# dockerを起動

- docker compose up

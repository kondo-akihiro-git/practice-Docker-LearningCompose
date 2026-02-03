# プロジェクト作成

- npx create-react-app react-app --no-git

# docker-compose.yml作成

```yml
version: '3.8'

services:
  react:
    image: node:20
    container_name: react-container
    working_dir: /app
    volumes:
      - ./:/app
    ports:
      - "3000:3000"
    command: >
      sh -c "npm install && npm start"
    user: "${UID}:${GID}"

```

# dockerを起動

- docker compose up

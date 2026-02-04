# docker-compose.yml作成

```yml
version: '3.8'

services:
  postgres:
    image: postgres:16
    container_name: postgres-container
    restart: always
    environment:
      POSTGRES_USER: sample_user
      POSTGRES_PASSWORD: sample_pass
      POSTGRES_DB: sample_db
    ports:
      - "5432:5432"
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  postgres-data:
```

# dockerを起動

- docker compose up -d

# 動作確認

- docker exec -it postgres-container bash
- psql -U sample_user -d sample_db


```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50)
);
INSERT INTO users (name) VALUES ('test_user');
SELECT * FROM users;

```

- docker compose down -v


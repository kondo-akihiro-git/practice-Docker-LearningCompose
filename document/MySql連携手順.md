# docker-compose.yml作成

```yml
version: '3.8'

services:
  mysql:
    image: mysql:8.0
    container_name: mysql-container
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: sample_db
      MYSQL_USER: sample_user
      MYSQL_PASSWORD: sample_pass
    ports:
      - "3306:3306"
    volumes:
      - mysql-data:/var/lib/mysql

volumes:
  mysql-data:

```

# dockerを起動

- docker compose up -d

# 動作確認

- docker exec -it mysql-container bash
- mysql -u root -p

```sql
USE sample_db;
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50)
);

INSERT INTO users (name) VALUES ('test_user');
SELECT * FROM users;
```

- docker compose down -v


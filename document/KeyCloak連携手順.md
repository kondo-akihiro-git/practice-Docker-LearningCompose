# docker-compose.yml作成

```yml
version: "3.8"

services:
  keycloak:
    image: quay.io/keycloak/keycloak:24.0
    container_name: keycloak
    command: start-dev
    ports:
      - "8080:8080"
    environment:
      KEYCLOAK_ADMIN: admin
      KEYCLOAK_ADMIN_PASSWORD: admin

```

# dockerを起動

- docker compose up -d

# 動作確認

- http://localhost:8080
    * ユーザーを作成

```bash
ACCESS_TOKEN=$(curl -s -X POST \
  http://localhost:8080/realms/master/protocol/openid-connect/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=password" \
  -d "client_id=admin-cli" \
  -d "username=admin" \
  -d "password=admin" \
| jq -r '.access_token')

curl -H "Authorization: Bearer $ACCESS_TOKEN" \
  http://localhost:8080/admin/realms/master/users
```
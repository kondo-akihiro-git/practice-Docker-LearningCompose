# docker-compose.yml作成

```yml
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.10.2
    container_name: es-container
    environment:
      - discovery.type=single-node # 分散型検索エンジンのためローカルで1台しかない場合はシングルノード設定を推奨
      - ES_JAVA_OPTS=-Xms512m -Xmx512m # ElasticSearch本体はJavaで動作する（起動時確保メモリとメモリ上限の設定が必要）
      - xpack.security.enabled=false
    ports:
      - "9200:9200"   # REST API
      - "9300:9300"   # クラスタ間通信
    volumes:
      - es-data:/usr/share/elasticsearch/data
    restart: always

volumes:
  es-data:

```

# dockerを起動

- docker compose up -d

# 動作確認

```bash
curl http://localhost:9200/

curl -X PUT "localhost:9200/users?pretty" \
     -H 'Content-Type: application/json' \
     -d '{
           "mappings": {
             "properties": {
               "name": { "type": "text" },
               "age":  { "type": "integer" }
             }
           }
         }'

curl -X POST "localhost:9200/users/_doc/1?pretty" \
     -H 'Content-Type: application/json' \
     -d '{
           "name": "test_1_user",
           "age": 30
         }'


curl -X POST "localhost:9200/users/_doc/2?pretty" \
     -H 'Content-Type: application/json' \
     -d '{
           "name": "test_2_user",
           "age": 28
         }'

curl -X GET "localhost:9200/users/_search?pretty" \
     -H 'Content-Type: application/json' \
     -d '{
           "query": {
             "match_all": {}
           }
         }'
```

- docker compose down -v

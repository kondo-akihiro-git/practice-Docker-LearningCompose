# docker-compose.yml作成

```yml
version: "3.9"

services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin

  blackbox:
    image: prom/blackbox-exporter:latest
    ports:
      - "9115:9115"

```

# prometheus.yml作成

```yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'blackbox'
    metrics_path: /probe
    params:
      module: [http_2xx]  # HTTP 200 をカウント
    static_configs:
      - targets:
          - http://example.com   # ここを監視したいURLに変更
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: blackbox:9115
```

# dockerを起動

- docker compose up -d

# 動作確認

Webアクセス
- http://localhost:9090
- http://localhost:3000
- http://localhost:9115
- Prometheusのエンドポイント: http://prometheus:9090
- Gradfanaのデータソース設定におけるターゲットメトリクス: count_over_time(probe_success[1h])


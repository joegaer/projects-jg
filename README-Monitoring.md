# Monitoring Stack
## Grafana · Prometheus · Node Exporter · Blackbox Exporter

### What is it?
A full monitoring stack for tracking system performance and service availability. Prometheus collects metrics, Node Exporter exposes host metrics, Blackbox Exporter probes services, and Grafana visualizes everything in graphs.

### Why did I install it?
To track CPU and memory usage over time like a task manager with history, and to monitor AdGuard availability including connection speed, processing time, and transfer speed.

### How They Work Together
* **Node Exporter** exposes host machine metrics (CPU, memory, disk, etc.)
* **Blackbox Exporter** probes AdGuard over HTTP and returns availability and response times
* **Prometheus** scrapes both every 15 seconds and stores the data
* **Grafana** connects to Prometheus and displays everything as graphs

### compose.yaml

```yaml
services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prom_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
    ports:
      - "9090:9090"
    restart: unless-stopped

  node-exporter:
    image: prom/node-exporter:latest
    container_name: node-exporter
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.sysfs=/host/sys'
      - '--path.rootfs=/rootfs'
    ports:
      - "9100:9100"
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3100:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    restart: unless-stopped

  blackbox-exporter:
    image: prom/blackbox-exporter:latest
    container_name: blackbox-exporter
    ports:
      - "9115:9115"
    restart: unless-stopped

volumes:
  prom_data:
  grafana_data:
```

### prometheus.yml

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'node-metrics'
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: 'adguard-status'
    metrics_path: /probe
    params:
      module: [http_2xx]
    static_configs:
      - targets:
          - http://192.168.1.x #IP placeholder
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: blackbox-exporter:9115
```

### What Prometheus is Scraping
* **node-metrics** — host machine metrics from Node Exporter every 15s
* **adguard-status** — probing AdGuard at `192.168.1.5` via Blackbox Exporter, checking HTTP 200 response, connection speed, processing time, and transfer speed

**Monitoring Stack**



Grafana · Prometheus · Node Exporter · Blackbox Exporter

**What is it?**



A full monitoring stack for tracking system performance and service availability. Prometheus collects metrics, Node Exporter exposes host metrics, Blackbox Exporter probes services, and Grafana visualizes everything in graphs.

**Why did I install it?**



To track CPU and memory usage over time like a task manager with history, and to monitor AdGuard availability including connection speed, processing time, and transfer speed.



**How They Work Together**



&#x20;   Node Exporter exposes host machine metrics (CPU, memory, disk, etc.)

&#x20;   Blackbox Exporter probes AdGuard over HTTP and returns availability and response times

&#x20;   Prometheus scrapes both every 15 seconds and stores the data

&#x20;   Grafana connects to Prometheus and displays everything as graphs



**compose.yaml**



services:

&#x20; prometheus:

&#x20;   image: prom/prometheus:latest

&#x20;   container\_name: prometheus

&#x20;   volumes:

&#x20;     - ./prometheus.yml:/etc/prometheus/prometheus.yml

&#x20;     - prom\_data:/prometheus

&#x20;   command:

&#x20;     - '--config.file=/etc/prometheus/prometheus.yml'

&#x20;   ports:

&#x20;     - "9090:9090"

&#x20;   restart: unless-stopped



&#x20; node-exporter:

&#x20;   image: prom/node-exporter:latest

&#x20;   container\_name: node-exporter

&#x20;   volumes:

&#x20;     - /proc:/host/proc:ro

&#x20;     - /sys:/host/sys:ro

&#x20;     - /:/rootfs:ro

&#x20;   command:

&#x20;     - '--path.procfs=/host/proc'

&#x20;     - '--path.sysfs=/host/sys'

&#x20;     - '--path.rootfs=/rootfs'

&#x20;   ports:

&#x20;     - "9100:9100"

&#x20;   restart: unless-stopped



&#x20; grafana:

&#x20;   image: grafana/grafana:latest

&#x20;   container\_name: grafana

&#x20;   ports:

&#x20;     - "3100:3000"

&#x20;   volumes:

&#x20;     - grafana\_data:/var/lib/grafana

&#x20;   restart: unless-stopped



&#x20; blackbox-exporter:

&#x20;   image: prom/blackbox-exporter:latest

&#x20;   container\_name: blackbox-exporter

&#x20;   ports:

&#x20;     - "9115:9115"

&#x20;   restart: unless-stopped



volumes:

&#x20; prom\_data:

&#x20; grafana\_data:



prometheus.yml



global:

&#x20; scrape\_interval: 15s



scrape\_configs:

&#x20; - job\_name: 'node-metrics'

&#x20;   static\_configs:

&#x20;     - targets: \['node-exporter:9100']



&#x20; - job\_name: 'adguard-status'

&#x20;   metrics\_path: /probe

&#x20;   params:

&#x20;     module: \[http\_2xx]

&#x20;   static\_configs:

&#x20;     - targets:

&#x20;         - http://192.168.1.5

&#x20;   relabel\_configs:

&#x20;     - source\_labels: \[\_\_address\_\_]

&#x20;       target\_label: \_\_param\_target

&#x20;     - source\_labels: \[\_\_param\_target]

&#x20;       target\_label: instance

&#x20;     - target\_label: \_\_address\_\_

&#x20;       replacement: blackbox-exporter:9115



**What Prometheus is Scraping**



&#x20;   node-metrics — host machine metrics from Node Exporter every 15s

&#x20;   adguard-status — probing AdGuard at 192.168.1.5 via Blackbox Exporter, checking HTTP 200 response, connection speed, processing time, and transfer speed






# Nagios Core & Uptime Kuma

### What are they?
Two complementary monitoring tools. Uptime Kuma provides a clean UI for quick uptime checks and Discord alerts. Nagios Core provides deeper visibility into host and service metrics.

### Why did I install them?
To monitor homelab services and get Discord alerts when something goes down. Nagios gives more detail — load, processes, swap, partition usage — while Uptime Kuma gives a quick at-a-glance status dashboard.

### Docker Compose

```yaml
services:
  nagios:
    image: jasonrivers/nagios:latest
    container_name: nagios_core_engine
    ports:
      - "9000:80"
    volumes:
      - ./etc:/opt/nagios/etc
      - ./var:/opt/nagios/var
    environment:
      - NAGIOSADMIN_USER=nagiosadmin
      - NAGIOSADMIN_PASS=AdminPassword123
      - NAGIOSADMIN_TIMEZONE=America/New_York
    restart: always

  uptime-kuma:
    image: louislam/uptime-kuma:1
    container_name: uptime-kuma
    volumes:
      - ./uptime-kuma-data:/app/data
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - "3001:3001"
    restart: always
```

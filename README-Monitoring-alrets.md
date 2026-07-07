\# Nagios Core \& Uptime Kuma



\### What are they?

Two complementary monitoring tools. Uptime Kuma provides a clean UI for quick uptime checks and Discord alerts. Nagios Core provides deeper visibility into host and service metrics.



\### Why did I install them?

To monitor homelab services and get Discord alerts when something goes down. Nagios gives more detail — load, processes, swap, partition usage — while Uptime Kuma gives a quick at-a-glance status dashboard.



\### Docker Compose



```yaml

services:

&#x20; nagios:

&#x20;   image: jasonrivers/nagios:latest

&#x20;   container\_name: nagios\_core\_engine

&#x20;   ports:

&#x20;     - "9000:80"

&#x20;   volumes:

&#x20;     - ./etc:/opt/nagios/etc

&#x20;     - ./var:/opt/nagios/var

&#x20;   environment:

&#x20;     - NAGIOSADMIN\_USER=nagiosadmin

&#x20;     - NAGIOSADMIN\_PASS=AdminPassword123

&#x20;     - NAGIOSADMIN\_TIMEZONE=America/New\_York

&#x20;   restart: always



&#x20; uptime-kuma:

&#x20;   image: louislam/uptime-kuma:1

&#x20;   container\_name: uptime-kuma

&#x20;   volumes:

&#x20;     - ./uptime-kuma-data:/app/data

&#x20;     - /var/run/docker.sock:/var/run/docker.sock

&#x20;   ports:

&#x20;     - "3001:3001"

&#x20;   restart: always

```




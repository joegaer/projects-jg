\# AdGuard Home

\### What is it?

A network-wide DNS-based ad blocker and privacy filter. Blocks ads, malware, phishing, and tracking at the DNS level before it reaches your devices.



\### Why did I install it?

To block harmful websites, stop phishing links, and have the best possible ad blocking on all my personal devices. Only used on devices connected to the Tailscale network.



\### Docker Compose



```yaml

services:

&#x20; adguardhome:

&#x20;   image: adguard/adguardhome

&#x20;   ports:

&#x20;     - 53:53/tcp

&#x20;     - 53:53/udp

&#x20;     - 80:80/tcp

&#x20;     - 3000:3000/tcp

&#x20;   volumes:

&#x20;     - config:/opt/adguardhome/conf

&#x20;     - work:/opt/adguardhome/work

&#x20;   restart: always

volumes:

&#x20; config:

&#x20;   driver: local

&#x20; work:

&#x20;   driver: local

```




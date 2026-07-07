# AdGuard Home

### What is it?
A network-wide DNS-based ad blocker and privacy filter. Blocks ads, malware, phishing, and tracking at the DNS level before it reaches your devices.

### Why did I install it?
To block harmful websites, stop phishing links, and have the best possible ad blocking on all my personal devices. Only used on devices connected to the Tailscale network.

### Docker Compose

```yaml
services:
  adguardhome:
    image: adguard/adguardhome
    ports:
      - 53:53/tcp
      - 53:53/udp
      - 80:80/tcp
      - 3000:3000/tcp
    volumes:
      - config:/opt/adguardhome/conf
      - work:/opt/adguardhome/work
    restart: always
volumes:
  config:
    driver: local
  work:
    driver: local
```

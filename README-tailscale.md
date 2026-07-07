# Tailscale

### What is it?

A VPN mesh network that connects all your devices securely over the internet without needing to open ports or configure a router.

### Why did I install it?

To remotely access the homelab server and all its services from anywhere. Also used as an exit node so all internet traffic from connected devices routes through the homelab.

### docker-compose.yml

```yaml
services:
  tailscale:
    network_mode: "host"
    image: tailscale/tailscale:latest
    container_name: tailscale
    hostname: docker-tailscale
    environment:
      - TS_HOSTNAME=docker-tailscale
      - TS_STATE_DIR=/var/lib/tailscale
      - TS_EXTRA_ARGS=--accept-dns=false --advertise-exit-node
    volumes:
      - ./state:/var/lib/tailscale
      - /dev/net/tun:/dev/net/tun
    cap_add:
      - NET_ADMIN
      - NET_RAW
    restart: unless-stopped
```

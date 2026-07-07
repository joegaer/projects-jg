Tailscale

What is it?



A VPN mesh network that connects all your devices securely over the internet without needing to open ports or configure a router.

Why did I install it?



To remotely access the homelab server and all its services from anywhere. Also used as an exit node so all internet traffic from connected devices routes through the homelab.

Access



&#x20;   Admin Console: https://login.tailscale.com/admin



docker-compose.yml



services:

&#x20; tailscale:

&#x20;   network\_mode: "host"

&#x20;   image: tailscale/tailscale:latest

&#x20;   container\_name: tailscale

&#x20;   hostname: docker-tailscale

&#x20;   environment:

&#x20;     - TS\_HOSTNAME=docker-tailscale

&#x20;     - TS\_STATE\_DIR=/var/lib/tailscale

&#x20;     - TS\_EXTRA\_ARGS=--accept-dns=false --advertise-exit-node

&#x20;   volumes:

&#x20;     - ./state:/var/lib/tailscale

&#x20;     - /dev/net/tun:/dev/net/tun

&#x20;   cap\_add:

&#x20;     - NET\_ADMIN

&#x20;     - NET\_RAW

&#x20;   restart: unless-stopped


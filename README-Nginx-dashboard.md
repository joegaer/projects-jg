# Core Routing & Portal Layer
## Cloudflare Tunnel · Nginx Proxy Manager · Flame Dashboard

### What is it?
A centralized inbound traffic routing and visual landing layer. Acts as a single secure gateway into the server, routing domain traffic into applications while providing a unified homepage to view and launch tools.

### Why did I install it?
To fix a port 80 conflict with AdGuard by shifting web traffic to port 8090, eliminate the need to remember individual ports for each service, and replace bookmarked subdomains with a clean visual launchpad at go.joekoda.com.

### How They Work Together
* Cloudflare Tunnel catches public traffic at `*.joekoda.com` and sends it into the network on port 8090.
* Nginx Proxy Manager listens on port 8090, reads the domain name, and forwards to the correct internal port.
* Flame Dashboard sits inside Nginx's network and serves as the visual launcher.

### compose.yaml

```yaml
services:
  # 1. Traffic Routing Engine
  nginx-proxy-manager:
    image: 'jc21/nginx-proxy-manager:latest'
    container_name: nginx-proxy-manager
    restart: unless-stopped
    ports:
      - '8090:80'   # Standard HTTP host access (Safe from AdGuard port 80)
      - '8091:81'   # Admin Web Dashboard UI
    volumes:
      - ./nginx/data:/data
      - ./nginx/letsencrypt:/etc/letsencrypt
    networks:
      - routing-net
 
  # 2. Cloudflare Tunnel Gateway
  cloudflare-tunnel:
    image: cloudflare/cloudflared:latest
    container_name: cloudflare-tunnel
    restart: unless-stopped
    environment:
      - TUNNEL_TOKEN=<mytoken>
    command: tunnel --no-autoupdate run
    network_mode: "host" # Allows the tunnel to see port 8090 directly on your server

  # 3. Dashboard UI
  flame-dashboard:
    image: 'pawelmalak/flame:latest'
    container_name: flame-dashboard
    restart: unless-stopped
    volumes:
      - ./flame/data:/app/data
    network_mode: "service:nginx-proxy-manager" # This embeds Flame right inside Nginx's space
    environment:
      - PASSWORD=<mypass>

networks:
  routing-net:
    driver: bridge
```

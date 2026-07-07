# Cloudflare Tunnel

### What is it?

A secure tunnel that connects the homelab to Cloudflare without needing to open any ports or expose the server directly to the internet. Also used with Cloudflare Access to put login gates on private services.

### Why did I install it?

To access all other homelab services remotely via subdomains without port forwarding. Cloudflare Access protects private services behind an email login gate.

### compose.yaml

```yaml
services:
  cloudflared:
    image: cloudflare/cloudflared:latest
    container_name: cloudflared
    command: tunnel --no-autoupdate run --token YOUR_TOKEN
    dns:
      - 1.1.1.1
      - 8.8.8.8
    restart: unless-stopped
```

\# Cloudflare Tunnel



\### What is it?

A secure tunnel that connects the homelab to Cloudflare without needing to open any ports or expose the server directly to the internet. Also used with Cloudflare Access to put login gates on private services.



\### Why did I install it?

To share the DokuWiki documentation publicly at `wiki.joekoda.com` and to access all other homelab services remotely via subdomains without port forwarding. Cloudflare Access protects private services behind an email login gate.



\### compose.yaml



```yaml

services:

&#x20; cloudflared:

&#x20;   image: cloudflare/cloudflared:latest

&#x20;   container\_name: cloudflared

&#x20;   command: tunnel --no-autoupdate run --token YOUR\_TOKEN

&#x20;   dns:

&#x20;     - 1.1.1.1

&#x20;     - 8.8.8.8

&#x20;   restart: unless-stopped

```




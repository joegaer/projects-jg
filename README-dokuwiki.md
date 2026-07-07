# DokuWiki

### What is it?
A simple flat-file wiki with no database required. Used as the documentation platform for this homelab.

### Why did I install it?
To document everything done on the homelab — services, configs, runbooks, and notes.

### Access

### compose.yaml

```yaml
services:
  dokuwiki:
    image: lscr.io/linuxserver/dokuwiki:latest
    container_name: dokuwiki
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=America/New_York
    volumes:
      - ./dokuwiki/config:/config
    ports:
      - 8081:80
      - 8443:443
    restart: unless-stopped
```

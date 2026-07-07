DokuWiki

What is it?



A simple flat-file wiki with no database required. Used as the documentation platform for this homelab.

Why did I install it?



To document everything done on the homelab — services, configs, runbooks, and notes.

Access







compose.yaml



services:

&#x20; dokuwiki:

&#x20;   image: lscr.io/linuxserver/dokuwiki:latest

&#x20;   container\_name: dokuwiki

&#x20;   environment:

&#x20;     - PUID=1000

&#x20;     - PGID=1000

&#x20;     - TZ=America/New\_York

&#x20;   volumes:

&#x20;     - ./dokuwiki/config:/config

&#x20;   ports:

&#x20;     - 8081:80

&#x20;     - 8443:443

&#x20;   restart: unless-stopped


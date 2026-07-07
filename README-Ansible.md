Ansible

What is it?



An open-source, agentless IT automation engine used for configuration management, system updates, and application deployment.

Why did I install it?



To quickly update packages, clean system bloat, and handle necessary reboots with a single command across my machine.



hosts



\[homelab]

192.168.1.5 ansible\_user=joe



update.yml



\---

\- name: Update and upgrade Ubuntu server

&#x20; hosts: homelab

&#x20; become: yes

&#x20; tasks:

&#x20;   - name: Run apt update and upgrade

&#x20;     ansible.builtin.apt:

&#x20;       update\_cache: yes

&#x20;       upgrade: safe



&#x20;   - name: Remove redundant packages

&#x20;     ansible.builtin.apt:

&#x20;       autoremove: yes



&#x20;   - name: Find all directories with a docker compose file

&#x20;     ansible.builtin.find:

&#x20;       paths: /home/joe

&#x20;       file\_type: directory

&#x20;       recurse: no

&#x20;     register: found\_directories



&#x20;   - name: Run docker compose update in every found folder

&#x20;     ansible.builtin.command:

&#x20;       cmd: docker compose pull \&\& docker compose up -d

&#x20;       chdir: "{{ item.path }}"

&#x20;     with\_items: "{{ found\_directories.files }}"

&#x20;     # This skips folders that don't have a compose file so it never errors out

&#x20;     failed\_when: false



&#x20;   - name: Ensure today's date header exists at the top of the changelog

&#x20;     ansible.builtin.lineinfile:

&#x20;       path: /home/joe/dokuwiki/dokuwiki/config/dokuwiki/data/pages/changelog.txt

&#x20;       create: true

&#x20;       line: "==== {{ \['','January','February','March','April','May','June','July','August','September','October','November','December']\[ansible\_facts\['date\_time']\['month'] | int] }} {{ ansible\_facts\['date\_time']\['day'] | int }} {{ ansible\_facts\['date\_time']\['year'] }} ===="

&#x20;       insertafter: "Newest entries at the top."



&#x20;   - name: Insert update entry directly under today's date header

&#x20;      ansible.builtin.lineinfile:

&#x20;        path: /home/joe/dokuwiki/dokuwiki/config/dokuwiki/data/pages/changelog.txt

&#x20;        line: "  \* \*\*{{ ansible\_facts\['date\_time']\['hour'] }}:{{ ansible\_facts\['date\_time']\['minute'] }}:{{ ansible\_facts\['date\_time']\['second'] }}\*\* - Automated maintenance: System packages and all Docker container stacks successfully updated."

&#x20;        insertafter: "==== {{ \['','January','February','March','April','May','June','July','August','September','October','November','December']\[ansible\_facts\['date\_time']\['month'] | int] }} {{ ansible\_facts\['date\_time']\['day'] | int }} {{ ansible\_facts\['date\_time']\['year'] }} ===="

&#x20;

&#x20; # Place these right after your docker compose task block

&#x20;   - name: Check if a system reboot is required

&#x20;     ansible.builtin.stat:

&#x20;       path: /var/run/reboot-required

&#x20;     register: reboot\_flag



&#x20;   - name: Reboot server if required by updates

&#x20;     ansible.builtin.reboot:

&#x20;       msg: "Rebooting homelab server after system updates..."

&#x20;     when: reboot\_flag.stat.exists


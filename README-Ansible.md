# Ansible

### What is it?
An open-source, agentless IT automation engine used for configuration management, system updates, and application deployment.

### Why did I install it?
To quickly update packages, clean system bloat, and handle necessary reboots with a single command across my machine.

### hosts

```ini
[homelab]
192.168.1.5 ansible_user=joe
```

### update.yml

```yaml
---
- name: Update and upgrade Ubuntu server
  hosts: homelab
  become: yes
  tasks:
    - name: Run apt update and upgrade
      ansible.builtin.apt:
        update_cache: yes
        upgrade: safe

    - name: Remove redundant packages
      ansible.builtin.apt:
        autoremove: yes

    - name: Find all directories with a docker compose file
      ansible.builtin.find:
        paths: /home/joe
        file_type: directory
        recurse: no
      register: found_directories

    - name: Run docker compose update in every found folder
      ansible.builtin.command:
        cmd: docker compose pull && docker compose up -d
        chdir: "{{ item.path }}"
      with_items: "{{ found_directories.files }}"
      # This skips folders that don't have a compose file so it never errors out
      failed_when: false

    - name: Ensure today's date header exists at the top of the changelog
      ansible.builtin.lineinfile:
        path: /home/joe/dokuwiki/dokuwiki/config/dokuwiki/data/pages/changelog.txt
        create: true
        line: "==== {{ ['','January','February','March','April','May','June','July','August','September','October','November','December'][ansible_facts['date_time']['month'] | int] }} {{ ansible_facts['date_time']['day'] | int }} {{ ansible_facts['date_time']['year'] }} ===="
        insertafter: "Newest entries at the top."

    - name: Insert update entry directly under today's date header
      ansible.builtin.lineinfile:
        path: /home/joe/dokuwiki/dokuwiki/config/dokuwiki/data/pages/changelog.txt
        line: "  * **{{ ansible_facts['date_time']['hour'] }}:{{ ansible_facts['date_time']['minute'] }}:{{ ansible_facts['date_time']['second'] }}** - Automated maintenance: System packages and all Docker container stacks successfully updated."
        insertafter: "==== {{ ['','January','February','March','April','May','June','July','August','September','October','November','December'][ansible_facts['date_time']['month'] | int] }} {{ ansible_facts['date_time']['day'] | int }} {{ ansible_facts['date_time']['year'] }} ===="
 
    # Place these right after your docker compose task block
    - name: Check if a system reboot is required
      ansible.builtin.stat:
        path: /var/run/reboot-required
      register: reboot_flag

    - name: Reboot server if required by updates
      ansible.builtin.reboot:
        msg: "Rebooting homelab server after system updates..."
      when: reboot_flag.stat.exists
```

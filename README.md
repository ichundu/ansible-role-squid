Role Name: squid
================

Installs and allows flexible configuration of squid with parameterized variables.

Requirements
------------

None.

Role Variables
--------------

All the sections in the squid configuration file `/etc/squid/squid.conf` template are parameterized with variables, to make the configuration as flexible as possible.
The configuration sections are defined by the following variables:

|   Variable name   |   Description   |
|-------------------|-----------------|
| `squid_acl_localnet` | ACLs for local networks |
| `squid_acl_defaults` | Default ACLs |
| `squid_acl_custom` | Custom ACLs |
| `squid_http_access` | HTTP access permissions |
| `squid_http_ports` | Squid http listen ports |
| `squid_cache_peer` | Cache peers |
| `squid_cache_peers_access` | Cache peers access |
| `squid_cache_dir` | Disck cache directory |
| `squid_coredump_dir` | Directory to leave coredumps |
| `squid_refresh_patterns` | `refresh_pattern` entries |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: squid
      squid_http_ports:
        - 3128
        - 80
```

License
-------

GPLv2

Author Information
------------------

https://github.com/ichundu

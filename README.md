# Dubzland: Shorewall

Installs and configures the Shorewall firewall builder.

## Requirements

Ansible version 2.0 or higher.

## Role Variables

Variable | Dictionary / Options
--- | ---
[dubzland_shorewall_interfaces](#dubzland_shorewall_interfaces) | network
interfaces shorewall will handle
[dubzland_shorewall_zones](#dubzland_shorewall_zones) | zones to be monitored
dubzland_shorewall_policies | moar stuff
dubzland_shorewall_masquerade | wow
dubzland_shorewall_rules | so bad

### <a id="dubzland_shorewall_zones"></a>dubzland_shorewall_zones

Zones to be declared in `/etc/shorewall/zones`.  See the [zones man
page](https://www.shorewall.net/manpages/shorewall-zones.html) for more info.

**example**
```yaml
dubzland_shorewall_zones:
  - name: fw
    type: firewall
  - name: net
    type: ipv4
  - name: lan
    type: ipv4
```

### <a id="dubzland_shorewall_interfaces"></a>dubzland_shorewall_interfaces

List of interfaces shorewall should be configured for.

**example**
```yaml
dubzland_shorewall_interfaces:
  - name: eth0
    zone: net
    options:
      - tcpflags
      - nosmurfs
      - sourceroute=0
  - name: eth1
    zone: lan
    options:
      - tcpflags
      - nosmurfs
      - logmartians
      - dhcp
```

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).

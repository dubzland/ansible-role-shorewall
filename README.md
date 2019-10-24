# Dubzland: Shorewall

Installs and configures the Shorewall firewall builder.

## Requirements

Ansible version 2.0 or higher.

## Role Variables

```yaml
dubzland_shorewall_zones:
  - { name: fw, type: firewall }
  - { name: net, type: ipv4 }

dubzland_shorewall_interfaces:
  - { name: eth0, zone: net, options: ['tcpflags', 'nosmurfs', 'routefilter', 'logmartians', 'sourceroute=0'] }

dubzland_shorewall_policies:
  - { source: "$FW", dest: all, policy: ACCEPT }
  - { source: net, dest: all, policy: REJECT }
  - { source: all, dest: all, policy: REJECT, log_level: info }

dubzland_shorewall_masquerade:
  enabled: False

dubzland_shorewall_rules:
  - section: NEW
    rulesets:
      - comment: PINGS
        rules: { action: "Ping(ACCEPT)", source: all, dest: all }
      - comment: Web traffic
        rules: { action: "Web(ACCEPT)", source: "$FW", dest: net }
        rules: { action: "ACCEPT", source: "$FW", dest: net, proto: udp, test_ports: [80, 443] }
```

### dubzland_shorewall_interfaces

List of interfaces shorewall should be configured for in
`/etc/shorewall/interfaces`.  See the [interfaces man
page](https://www.shorewall.net/manpages/shorewall-interfaces.html) for more info.

**example**
```yaml
dubzland_shorewall_interfaces:
  - name: eth0
    zone: net
    options:
      - tcpflags
      - nosmurfs
      - sourceroute=0
```

### dubzland_shorewall_zones

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

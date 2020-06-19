# Dubzland: Shorewall
[![Gitlab pipeline status (self-hosted)](https://img.shields.io/gitlab/pipeline/jdubz/dubzland-shorewall?gitlab_url=https%3A%2F%2Fgit.dubzland.net)](https://git.dubzland.net/jdubz/dubzland-shorewall/pipelines)

Installs and configures the Shorewall firewall builder.

## Requirements

Ansible version 2.0 or higher.  Requires the `netaddr` python package.

## Role Variables

Available variables are listed below, along with their default values (see
    `defaults/main.yml` for more info):

### dubzland_shorewall_conf

```yaml
dubzland_shorewall_conf:
  startup_enabled: "Yes"
  verbosity: 1
  log_level: '"info"'
  log_martians: "Yes"
  log_verbosity: 2
  log_zone: Both
  logfile: /var/log/shorewall
  logformat: '"%s(%d) %s "'
```

Options to be set in `/etc/shorewall/shorewall.conf`.  Option names can be specified in either upper- or lower-case (they will be written in all caps to the file).  See the [shorewall.conf man page](http://www.shorewall.net/manpages/shorewall.conf.html) for more info.

### dubzland_shorewall_params

```yaml
dubzland_shorewall_params: []
```

List of key-value pairs to be written to `/etc/shorewall/params`.  For more information on using params, see the [params man page](http://www.shorewall.net/manpages/shorewall-params.html).

### dubzland_shorewall_zones

```yaml
dubzland_shorewall_zones:
  - name: fw
    type: firewall
  - name: net
    type: ipv4
  - name: lan
    type: ipv4
```

Zones to be declared in `/etc/shorewall/zones`.  See the [zones man page](http://www.shorewall.net/manpages/shorewall-zones.html) for more info.


### dubzland_shorewall_interfaces

```yaml
dubzland_shorewall_interfaces:
  - name: eth0
    zone: net
    options:
      - tcpflags
      - nosmurfs
      - routefilter
      - "sourceroute=0"
  - name: eth1
    zone: lan
    options:
      - tcpflags
      - nosmurfs
      - routefilter
```

List of interfaces shorewall should be configured for in `/etc/shorewall/interfaces`.  See the [interfaces man page](http://www.shorewall.net/manpages/shorewall-interfaces.html) for more info.

### dubzland_shorewall_hosts

```yaml
dubzland_shorewall_hosts: []
```

Specifies hosts routable, but not directly accessible, by the firewall machine.

### dubzland_shorewall_policies

```yaml
dubzland_shorewall_policies:
  - source: "$FW"
    dest: all
    policy: ACCEPT
  - source: net
    dest: all
    policy: REJECT
  - source: all
    dest: all
    policy: REJECT
    log_level: info
```

Policies used by Shorewall to determine the default action to take for a given packet based on its zone traversal.  See the [policy man page](http://www.shorewall.net/manpages/shorewall-policy.html) for more info.


### dubzland_shorewall_snat

```yaml
dubzland_shorewall_snat:
  - action: MASQUERADE
    dest: eth0
```

Configures SNAT/Masquerading for iptables.  Necessary if you want to perform network address translation (NAT) on outbound traffic.  See the [snat man page](http://www.shorewall.net/manpages/shorewall-snat.html) for more info.

### dubzland_shorewall_rules

```yaml
dubzland_shorewall_rules:
  - section: NEW
    rulesets:
      - comment: PINGS
        rules:
          - action: Ping(ACCEPT)
            source: all
            dest: all
      - comment: Web traffic
        rules:
          - action: Web(ACCEPT)
            source: $FW,lan
            dest: net
```

The meat of this role.  Configures the rules Shorewall will use to determine how to handle packets traversing its monitored interfaces.  See the [rules man page](http://www.shorewall.net/manpages/shorewall-rules.html) for more info.

## Dependencies

None.

## Example Playbook

Given a machine with 2 nics (`eth0` on the internet, `eth1` on the LAN):

```yaml
- hosts: firewall
  become: yes
  roles:
    - role: dubzland-shorewall
      vars:
        dubzland_shorewall_zones:
          - name: fw
            type: firewall
          - name: net
            type: ipv4
          - name: lan
            type: ipv4
        dubzland_shorewall_interfaces:
          - name: eth0
            zone: net
            options:
              - tcpflags
              - nosmurfs
              - routefilter
              - "sourceroute=0"
          - name: eth1
            zone: lan
            options:
              - tcpflags
              - nosmurfs
              - routefilter
        dubzland_shorewall_policies:
          - source: "$FW"
            dest: all
            policy: ACCEPT
          - source: net
            dest: all
            policy: REJECT
          - source: all
            dest: all
            policy: REJECT
            log_level: info
        dubzland_shorewall_snat:
          - action: MASQUERADE
            dest: eth0
        dubzland_shorewall_rules:
          - section: NEW
            rulesets:
              - comment: Pings
                rules:
                  - action: Ping(ACCEPT)
                    source: all
                    dest: all
              - comment: Web Surfing
                rules:
                  - action: Web(ACCEPT)
                    source: lan
                    dest: net
                  - action: ACCEPT
                    source: lan
                    dest: net
                    proto: udp
                    dest_ports:
                      - 80
                      - 443
```

This would everyone to ping the firewall machine, and LAN clients to ping hosts
on the internet.  All LAN clients would also be able to browse the web.

## License

MIT

## Author

* [Josh Williams](https://codingprime.com)

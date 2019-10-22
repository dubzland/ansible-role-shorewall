#!/bin/sh
ansible-playbook -i /usr/src/dubzland-shorewall/tests/inventory.yml -e skip_handlers=true /usr/src/dubzland-shorewall/tests/test.yml

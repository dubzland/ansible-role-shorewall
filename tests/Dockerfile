FROM jdubz/gitlab-debian-ansible:latest

WORKDIR /usr/src/dubzland-shorewall

RUN mkdir -p /usr/src/dubzland-shorewall

ADD . /usr/src/dubzland-shorewall

ENV ANSIBLE_ROLES_PATH=/usr/src

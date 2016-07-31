#!/bin/bash
listening=`/usr/sbin/lsof -i :5900`
if [[ '' == $listening ]]; then
    cd /root
    bash restart.sh
fi

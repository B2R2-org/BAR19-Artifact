#!/bin/sh
readonly mnthost=$(dirname $(readlink -f $0))/../blobs
readonly mntguest=/expbin

docker run -v /etc/localtime:/etc/localtime:ro --net=host --cpus=${2} -it -v ${mnthost}:${mntguest} ${1} /bin/bash

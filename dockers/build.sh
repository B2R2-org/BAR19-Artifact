#!/bin/sh

docker build --network=host -t ${1} ./${1}/

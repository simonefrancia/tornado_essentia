#!/bin/bash
#
# @author Alberto Soragna (alberto dot soragna at gmail dot com)
# @2018

[ -z "$BASE_NAME" ] && { echo "Missing environment. Please run first"; echo "source env.sh"; exit 1; }

VERSION=$1

[ -z "$VERSION" ] && { echo "Usage: $0 VERSION"; exit 1; }

echo Using:
echo Volume path:$VOL_CONTAINER_PATH \$VOL_CONTAINER_PATH
echo Base container:$BASE_CONTAINER \$BASE_CONTAINER
echo Base image:$BASE_NAME \$BASE_NAME
echo Version: $VERSION


CMD=bash

## Simple run
#docker run -it --name $BASE_NAME $BASE_CONTAINER:$VERSION $CMD -v "/home/mxm/essentia_scripts":/essentia/tests

## Run with volume on data
#docker run -d -p 5000:5000 --name $BASE_NAME $BASE_CONTAINER:$VERSION $CMD
docker run -it -p 8888:8888 -v "`pwd`/src":/tornado_api/ --name $BASE_NAME $BASE_CONTAINER:$VERSION bash
#docker run --rm -it -v "/home/mxm/tornado/src":/src --name $BASE_NAME $BASE_CONTAINER:$VERSION $CMD

#!/bin/bash
#
# @author Simone Francia (simone dot francia at musixmatch dot com)
# @2018
echo Building $BASE_CONTAINER:$VERSION...


#docker build -t $BASE_CONTAINER:$VERSION .

docker build -t $BASE_CONTAINER:$VERSION .

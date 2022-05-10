#!/bin/bash

docker run -p 8000:8000 --mount type=bind,source=$1,target=/blackalex firekeeper-server-test

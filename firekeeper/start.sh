#!/bin/bash

gunicorn firekeeper.wsgi --bind 0.0.0.0:8000 --timeout 500

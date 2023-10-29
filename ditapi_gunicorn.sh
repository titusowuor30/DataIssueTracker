#!/bin/bash

. /home/tech/DataIssueTracker/env/bin/activate  # Activate your virtual environment
cd /home/tech/DataIssueTracker/

nohup gunicorn --bind 0.0.0.0:8000 DITApi.wsgi:application > /home/tech/trackerlogs/ditapilogfile.log 2>&1 &

#!/bin/sh
python /code/service.py &
envoy -l info -c /etc/service-envoy.yaml --service-node serviceA-service --service-cluster serviceA-cluster

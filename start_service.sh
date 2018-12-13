#!/bin/sh
python3 /code/service.py &
envoy --v2-config-only -l info -c /etc/service-envoy.yaml --service-node serviceA-service --service-cluster serviceA-cluster

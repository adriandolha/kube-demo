#!/usr/bin/env bash
helm install stable/grafana -f grafana-values.yaml
kubectl delete -f grafana-service.yaml
kubectl apply -f grafana-service.yaml


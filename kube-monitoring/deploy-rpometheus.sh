#!/usr/bin/env bash
kubectl apply -f monitoring-namespace.yaml
kubectl apply -f prometheus-config.yaml
kubectl apply -f prometheus-deployment.yaml
kubectl apply -f prometheus-service.yaml
kubectl apply -f node-exporter-daemonset.yml

# custom metrics
#kubectl apply -f custom-metrics-config-map.yaml
#kubectl apply -f custom-metrics.yaml
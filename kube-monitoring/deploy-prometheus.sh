#!/usr/bin/env bash
kubectl apply -f monitoring-namespace.yaml
kubectl apply -f prometheus-config.yaml
kubectl delete -f prometheus-deployment.yaml --ignore-not-found
kubectl apply -f prometheus-deployment.yaml
kubectl apply -f prometheus-service.yaml
#kubectl apply -f node-exporter-daemonset.yml


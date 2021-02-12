#!/usr/bin/env bash
kubectl delete ns monitoring

kubectl apply -f monitoring-namespace.yaml
kubectl apply -f prometheus-config.yaml
kubectl delete -f prometheus-deployment.yaml --ignore-not-found
kubectl apply -f prometheus-deployment.yaml
kubectl apply -f prometheus-service.yaml

helm install --name grafana stable/grafana -f grafana-values.yaml
kubectl delete -f grafana-service.yaml
kubectl apply -f grafana-service.yaml


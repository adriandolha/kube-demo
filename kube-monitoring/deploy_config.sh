#!/usr/bin/env bash
kubectl delete cm prometheus-config -n monitoring
kubectl apply -f prometheus-config.yaml

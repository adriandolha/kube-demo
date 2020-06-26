#!/bin/bash
docker build -t from-service:dev .

kubectl -n demo delete deployment from-service --ignore-not-found
kubectl -n demo delete service from-service --ignore-not-found

kubectl apply -f pod.yaml
kubectl apply -f service.yaml

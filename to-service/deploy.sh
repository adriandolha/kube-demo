#!/bin/bash
docker build -t to-service:dev .

kubectl -n demo delete deployment to-service --ignore-not-found
kubectl -n demo delete service to-service --ignore-not-found

kubectl apply -f pod.yaml
kubectl apply -f service.yaml

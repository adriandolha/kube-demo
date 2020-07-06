#!/usr/bin/env bash
#kubectl delete -f ambassador-rbac.yaml --ignore-not-found
#kubectl delete -f ambassador-service.yaml --ignore-not-found
#kubectl delete -f httpbin.yaml --ignore-not-found
#kubectl apply -f ambassador-rbac.yaml
#kubectl apply -f ambassador-service.yaml
#kubectl apply -f httpbin.yaml
kubectl apply -f https://www.getambassador.io/yaml/aes-crds.yaml && \
kubectl wait --for condition=established --timeout=90s crd -lproduct=aes && \
kubectl apply -f https://www.getambassador.io/yaml/aes.yaml && \
kubectl -n ambassador wait --for condition=available --timeout=90s deploy -lproduct=aes
kubectl apply -f ambassador-proxy-protocol.yaml
# kube-demo
Kubernetes Demo

## Pre-requisites
There are a few tools that you need to have on your local environment before going forward.
* terraform
* helm
* kubernetes

### Helm
To install helm on your mac (https://helm.sh/docs/intro/install/):
```
brew install helm
```
#### Troubleshooting
##### Error: error installing: the server could not find the requested resource
Fix:
First, we need to install deploy service account:
```bash
kubectl apply -f tiller.yaml
```
where tiller.yaml is:
```yaml
kind: ServiceAccount
apiVersion: v1
metadata:
  name: tiller
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: tiller
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: ServiceAccount
    name: tiller
    namespace: kube-system
```
Next, init helm using the following command:
```bash
helm init --service-account tiller --override spec.selector.matchLabels.'name'='tiller',spec.selector.matchLabels.'app'='helm' --output yaml | sed 's@apiVersion: extensions/v1beta1@apiVersion: apps/v1@' | kubectl apply -f -
```

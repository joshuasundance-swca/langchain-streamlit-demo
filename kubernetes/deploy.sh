#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# Create a secret for environment variables
secretExists=$(kubectl get secret langchain-streamlit-demo-secret --ignore-not-found)

if [ -n "$secretExists" ]; then
  echo "Secret 'langchain-streamlit-demo-secret' already exists. Deleting and recreating."
  kubectl delete secret langchain-streamlit-demo-secret
else
  echo "Secret 'langchain-streamlit-demo-secret' does not exist. Creating."
fi

kubectl create secret generic langchain-streamlit-demo-secret --from-env-file=.env


# Deploy to Kubernetes
kubectl apply -f kubernetes/resources.yaml

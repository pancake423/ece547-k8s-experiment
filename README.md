# About

## Created For

ECE547 Final Project at NC State, Fall 2025.

## Purpose

Design a Kubernetes environment to experimentally validate some aspects of our overall design.

## Author

William Jackson

# Setup

## Prerequisites

This project requires [docker](https://www.docker.com/get-started/), [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/), [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation), and [cloud-provider-kind](https://github.com/kubernetes-sigs/cloud-provider-kind) to be installed.

## Running the K8S cluster

Note that these commands are for Ubuntu linux. For other systems, commands may vary slightly.
```bash
# create the cluster
sudo kind create cluster --config kind-config.yaml --name multi-node-cluster

# leave this command running in a separate terminal.
# run cloud-provider-kind to enable load balancers
sudo cloud-provider-kind

# deploy the metrics server (needed for HPA)
sudo kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
# apply patches to the metrics server needed to get it working w/ kind deployment
sudo kubectl apply -k .

# build the local server docker image and push it to the cluster
sudo docker build -t server:1.0 server
sudo kind load docker-image server:1.0 --name multi-node-cluster

# deploy the application
sudo kubectl apply -f deployment.yaml

# view the IP address of the load balancer (app entry point)
echo http://$(sudo kubectl get svc/app-service -o=jsonpath='{.status.loadBalancer.ingress[0].ip}'):8080

# view the status of the HPA
sudo kubectl get hpa

# delete one of the nodes (simulates an availability zone failure)
# can also delete multi-node-cluster-worker2 and 3.
sudo kubectl delete node multi-node-cluster-worker --force

# delete the cluster when done experimenting
sudo kind delete cluster --name multi-node-cluster
```

## Running the locust load generator

follow the instructions in [load-gen/README.md](load-gen/README.md)

# Sources Used

- https://medium.com/@rishikrohan/run-a-multi-node-kubernetes-cluster-locally-with-kind-9a7101d85743

- https://dev.to/i_am_vesh/multi-node-kubernetes-cluster-setup-with-kind-mih

- https://bytegoblin.io/blog/how-to-run-locally-built-docker-images-in-kubernetes

- https://www.codebuff.dev/blog/Kind-Cluster-LoadBalancer-Kubernetes

- https://github.com/damini112/k8s-hpa-metrics-server?tab=readme-ov-file

- https://gist.github.com/sanketsudake/a089e691286bf2189bfedf295222bd43

- official documentation for kind, kubernetes, and docker also used extensively.

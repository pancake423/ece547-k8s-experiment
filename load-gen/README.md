# About
locust load generator for testing k8s deployment,
and HPA monitoring dashboard.

# Setup

## Prerequisites
requires [uv](https://docs.astral.sh/uv/getting-started/installation/) (package manager for python).

```bash
# run locust
uv run locust -f locustfile.py

# run the k8s HPA monitor
uv run hpa-monitor.py
```

press enter to open the webpage for starting locust demos. You have to manually setup the load for locust. To get the host address, run
```bash
echo http://$(sudo kubectl get svc/app-service -o=jsonpath='{.status.loadBalancer.ingress[0].ip}'):8080
```
This command will echo the address of the application.

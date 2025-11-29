# About
locust load generator for testing k8s deployment,
and HPA monitoring dashboard.

# Setup

## Prerequisites
requires uv (package manager for python).

```bash
# run locust
uv run locust -f locustfile.py

# run the k8s HPA monitor
uv run hpa-monitor.py
```

press enter to open the webpage for starting locust demos.

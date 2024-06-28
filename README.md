# mqtt-prometheus-metrics

This repository contains a Python application that exports MQTT metrics to Prometheus. The application is packaged as a Docker container and can be deployed on a Kubernetes cluster using the provided Helm chart.

## Application

The Python application is located in the `src` directory, with the main file being `mqtt_prometheus_exporter.py`. It uses environment variables for MQTT connection information and starts a Flask server to expose the metrics. The application uses the `paho-mqtt` library for MQTT communication and the `prometheus_client` library for exposing Prometheus metrics. The Flask web framework is used to serve the `/metrics` endpoint.

## Docker

The Docker container is built using the provided `Containerfile`. The application dependencies are listed in the `requirements.txt` file. The Docker container exposes port 8088 and starts the application using gunicorn.

## Helm Chart

The Helm chart in the `chart` directory can be used to deploy the application on a Kubernetes cluster. The chart includes a Deployment, a Service, a ServiceMonitor for Prometheus Operator, and a VirtualService for Istio.

The `values.yaml` file in the chart directory contains the configuration values for the Helm chart. The image repository and tag, the service type and port, the ServiceMonitor configuration, and the gateway name can be set in this file.

The Helm chart deploys a Kubernetes Deployment with a single replica by default, using the image from `<repository>/mqtt-prometheus-metrics`. The Service exposes port 8088 on a ClusterIP. If enabled, a ServiceMonitor is created to scrape metrics from the `/metrics` endpoint every 30 seconds. A VirtualService is also created for Istio, routing all traffic to the Service.

The `ServiceMonitor.yaml` file is an example of how to create a ServiceMonitor for this application in a Prometheus Operator setup.

Remember to commit and push your changes to the repository after updating the `README.md` file.# mqtt-prometheus-metrics
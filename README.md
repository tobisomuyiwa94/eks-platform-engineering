# EKS Platform Engineering

A hands-on Platform Engineering project demonstrating containerization, Kubernetes deployment patterns, Helm-based application packaging, and infrastructure-as-code concepts.

## Objectives

- Build and containerize a lightweight application.
- Define reusable Kubernetes deployment resources.
- Package Kubernetes resources with Helm.
- Explore AWS infrastructure provisioning with Terraform.
- Develop CI/CD automation and observability practices.
- Validate components locally before provisioning cloud resources.

## Technology Stack

- Python
- Docker
- Kubernetes
- Helm 3
- Terraform
- AWS / Amazon EKS
- Git and GitHub

## Application

The Python application exposes two HTTP endpoints:

- `/` — Returns a welcome message.
- `/health` — Returns the application's health status.

The Docker image uses Python 3.12 slim and runs the application as a non-root user.

## Kubernetes

The `kubernetes/` directory contains manifests for a dedicated namespace, a Deployment, and a ClusterIP Service.

The Deployment defines one replica, CPU and memory requests and limits, and readiness and liveness probes that use `/health`.

The Service exposes port 80 and forwards traffic to container port 8080.

## Helm Chart

The Helm chart is located at `helm/platform-app/`.

```text
helm/platform-app/
├── Chart.yaml
├── values.yaml
└── templates/
    ├── deployment.yaml
    └── service.yaml
```

The chart uses configurable values for the container image, replica count, service ports, resource limits, and health-check path.

### Local Helm Validation

The chart has passed linting with zero failures, and its Deployment and Service templates have rendered successfully.

```bash
helm lint helm/platform-app
helm template platform-demo helm/platform-app --namespace platform-demo
```

## Local Development

Run the Python application:

```bash
python3 app/app.py
```

Test the health endpoint in another terminal:

```bash
curl http://localhost:8080/health
```

Build the Docker image from the repository root:

```bash
docker build -t platform-demo:1.0 .
```

Run the container:

```bash
docker run --rm --name platform-demo -p 8080:8080 platform-demo:1.0
```

Then visit `http://localhost:8080/health`.

## Repository Structure

```text
.
├── app/
├── helm/
│   └── platform-app/
├── infrastructure/
│   └── terraform/
├── kubernetes/
│   ├── configs/
│   ├── deployments/
│   ├── namespaces/
│   └── services/
├── scripts/
├── Dockerfile
└── README.md
```

## Cost Management

AWS resources will be provisioned only when needed for testing and demonstrations. Resources will be reviewed and destroyed when no longer required to minimize unnecessary charges.

## Project Status

### Completed
- Python application and health endpoint.
- Local Docker image build and container testing.
- Kubernetes namespace, Deployment, and Service manifests.
- Helm chart implementation.
- Helm linting and template rendering.
- GitHub version control and publishing.

### In Progress
- Troubleshooting local Kubernetes cluster startup.
- Preparing for Kubernetes deployment and runtime verification.

### Planned
- AWS EKS infrastructure provisioning.
- CI/CD automation.
- Monitoring and observability.

**Deployment status:** The application has not yet been verified on a running Kubernetes cluster or deployed to AWS. Current validation covers local application/container testing and Helm chart rendering.

## Implementation Status

- [x] Python HTTP application with homepage and health endpoints
- [x] Docker image built and tested locally
- [x] Kubernetes manifests for Namespace, Deployment, and Service
- [x] Helm chart created and validated
- [x] Local Kubernetes cluster created with kind
- [x] Application deployed through Helm
- [x] Kubernetes Deployment and Pod verified healthy
- [x] Kubernetes Service tested through port forwarding
- [x] Health and homepage endpoints returned expected JSON responses

### Validation Results

The application was deployed to a local kind Kubernetes cluster using the `platform-demo:1.0` Docker image and the project's Helm chart.

- **Deployment:** 1/1 replicas available
- **Pod:** Running with zero restarts at verification
- **Service:** ClusterIP on port 80, forwarding to container port 8080
- **Health endpoint:** `/health` returned `{"status": "healthy", "service": "platform-demo"}`
- **Homepage:** `/` returned the expected application message

This project has been validated locally. A cloud-based AWS EKS deployment has not been performed.
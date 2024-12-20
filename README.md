# Guillermo Aka Maverick - DevOps Exercise

## Introduction

This repository contains services designed to handle GET and POST endpoints, leveraging technologies like Kubernetes (k8s), Docker, CI/CD, GNU/Linux, Python, and web development. It demonstrates a scalable and robust architecture for deploying web applications.

---

## Setting Up Your Environment

Follow these steps to prepare your environment:

### 1. Fork and Clone the Repository

1. Ensure GitHub is installed on your machine:
   ```bash
   github --help
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/GuilleX69/devops-exercise.git
   ```
3. Confirm you are logged in to GitHub via SSH:
   - Generate a new SSH key:
     ```bash
     ssh-keygen
     ```
   - Copy the contents of `id_rsa.pub` and add it to your GitHub SSH keys under `Settings > SSH and GPG keys`.

### 2. Install Docker

1. Install Docker:
   ```bash
   sudo apt install docker.io
   ```
2. Verify installation:
   ```bash
   docker ps
   ```

### 3. Access a Kubernetes Cluster

You can use Minikube or any other Kubernetes provider. To install Kubernetes tools on Linux:
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client
```

### 4. Run the Applications

Once the environment is set up, proceed to run the services.

---

## Running the Application

### Pull the Docker Image

1. Pull the image from Docker Hub:
   ```bash
   docker pull x69420x/guillermo-ramirez
   ```
2. Verify the image:
   ```bash
   docker image ls
   ```
   Expected output:
   ```
   REPOSITORY                    TAG       IMAGE ID       CREATED             SIZE
   x69420x/guillermo-ramirez     latest    9441b6af3b42   About an hour ago   138MB
   ```

### Run the Application

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 5000:5000 -p 5001:5001 x69420x/guillermo-ramirez
   ```

3. Access the application in your browser:
   - Visit [http://localhost:5000](http://localhost:5000).

   The app provides:
   - **Increment Counter**: Executes a POST request to increment a counter.
   - **Get Counter**: Executes a GET request to display the counter value.

---

## Deploying to Kubernetes

### Validate Your Cluster

1. Check cluster status:
   ```bash
   kubectl cluster-info
   kubectl config use-context minikube
   ```

2. Start Minikube:
   ```bash
   minikube start
   ```

3. Confirm status:
   ```bash
   minikube status
   ```

### Deploy the Services

1. Navigate to the Kubernetes deployment directory:
   ```bash
   cd k8s-deployments/
   ```
2. Deploy the services:
   ```bash
   kubectl apply -f post-service-deployment.yaml
   kubectl apply -f post-service-service.yaml
   ```
3. Verify the deployment:
   ```bash
   kubectl get pods
   kubectl get service post-service
   ```

### Expose the Service

1. Expose the service to the world:
   ```bash
   minikube service post-service
   ```
2. Access the service at the provided URL (e.g., [http://127.0.0.1:46521](http://127.0.0.1:46521)).

---

## References

- [Run a Stateless Application Using a Deployment](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/)


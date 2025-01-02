#!/bin/bash

install_packages() {
  echo "[+] Updating package index and installing required packages..."
  sudo apt update
  sudo apt install -y docker.io socat git net-tools
}

configure_docker() {
  echo "[+] Configuring Docker for $USER..."
  sudo usermod -aG docker $USER
  echo "Please log out and log back in to apply Docker group changes."
}

install_kubectl() {
  echo "[+] Installing kubectl..."
  curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
  sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
  chmod +x kubectl
  sudo mv kubectl /usr/local/bin/
}

install_minikube() {
  echo "[+] Installing Minikube..."
  curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
  sudo install minikube-linux-amd64 /usr/local/bin/minikube
  rm minikube-linux-amd64
}

start_minikube() {
  echo "[+] Starting Minikube..."
  minikube start
}

apply_k8s_deployments() {
  echo "[+] Applying Kubernetes deployments and services..."
  kubectl apply -f k8s-deployments/post-service-deployment.yaml
  kubectl apply -f k8s-deployments/post-service.yaml
}

setup_traffic_forwarding() {
  echo "[+] Setting up traffic forwarding to Minikube service..."
  TARGET=$(minikube service post-service --url | awk -F'/' '{print $3}')
  sudo socat TCP-LISTEN:80,fork TCP:$TARGET &
}

confirm_deployment() {
  echo "[+] Deployment confirmed. Access your service at:"
  minikube service post-service --url
}

main() {
  install_packages
  sleep 10
  
  configure_docker
  sleep 10

  install_kubectl
  sleep 10

  install_minikube
  sleep 10

  start_minikube
  sleep 10

  apply_k8s_deployments
  sleep 10

  setup_traffic_forwarding
  sleep 10

  confirm_deployment
  sleep 10
  
  echo "[+] Applications have been deployed successfully!"
}

main


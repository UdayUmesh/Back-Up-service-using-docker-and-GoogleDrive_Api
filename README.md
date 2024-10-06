# Backup Service Using Docker and Kubernetes

## Overview
This project implements a cloud-native backup service that periodically backs up the contents of a specified folder to Google Drive using Docker and Kubernetes. It leverages the Google Drive API for file storage, Docker for containerization, and Kubernetes for orchestration and automation.

## Table of Contents
1. [Features](#features)
2. [Pre-requisites](#pre-requisites)
3. [Setup and Installation](#setup-and-installation)
4. [Usage](#usage)
5. [Kubernetes Configuration](#kubernetes-configuration)
6. [Security](#security)
7. [Monitoring and Logging](#monitoring-and-logging)
8. [Future Enhancements](#future-enhancements)
9. [License](#license)

## Features
- **Automated backups**: Schedule periodic backups to Google Drive.
- **Containerized solution**: The entire service runs in a Docker container.
- **Kubernetes orchestration**: Automated backup tasks using Kubernetes CronJobs.
- **Persistent storage**: Utilizes Kubernetes Persistent Volume Claims (PVC) for storage.
- **Security**: API credentials are securely managed with Kubernetes Secrets.
- **Logging**: Logs the backup process for troubleshooting and validation.

## Pre-requisites
Ensure the following tools are installed on your system:
- Docker (Windows | Ubuntu | macOS)
- Kubernetes (Windows | Ubuntu | macOS)
- Google Cloud account with Google Drive API access

## Setup and Installation
### 1. Google Drive API Setup
- **Obtain API credentials**:
  - Visit the [Google Cloud Console](https://console.cloud.google.com/).
  - Enable the Google Drive API.
  - Create OAuth 2.0 credentials and download the `credentials.json` file.
  
- **Install required Python packages**:
  - Install `google-api-python-client` and other dependencies:
    ```bash
    pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```

### 2. Build the Docker Image
- **Dockerfile**:
  Create a `Dockerfile` that installs all dependencies and runs the backup script.
  
  ```Dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY . /app
  RUN pip install --no-cache-dir -r requirements.txt
  CMD ["python", "backup.py"]
  ```
- **Build the Docker image**:
  ```bash
  docker build -t backup-service .
  ```
- Run the container (replace /path/to/folder with the folder you want to back up):
  ```bash
  docker run -v /path/to/folder:/backup-folder backup-service
  ```

## Usage

### 1. Local Backup Execution
- Run the backup process locally within the Docker container to ensure everything works as expected before deploying it to Kubernetes.

### 2. Kubernetes Setup

#### 2.1. Deploy Using Kubernetes CronJob
- Define a Kubernetes CronJob to run the backup service at specified intervals:

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: backup-cronjob
spec:
  schedule: "0 */6 * * *" # Runs every 6 hours
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup-container
            image: backup-service:latest
            volumeMounts:
            - name: backup-pvc
              mountPath: /backup-folder
          restartPolicy: OnFailure
          volumes:
          - name: backup-pvc
            persistentVolumeClaim:
              claimName: backup-claim
```

- Apply the CronJob:

```bash
kubectl apply -f cronjob.yaml
```

#### 2.2. Persistent Volume Claim (PVC)
- Define a PVC to store the files for backup:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: backup-claim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

- Apply the PVC:

```bash
kubectl apply -f pvc.yaml
```

## Security
- Use Kubernetes Secrets to securely manage your API credentials:

```bash
kubectl create secret generic google-drive-credentials --from-file=credentials.json
```

## Monitoring and Logging
- Access logs to monitor the backup process:

```bash
kubectl logs <pod-name>
```

- Optionally, set up monitoring tools like Prometheus and Grafana for enhanced observability.

## Future Enhancements
- **Advanced monitoring**: Integrate tools like Prometheus and Grafana for alerting and monitoring backup failures.
- **Multi-cloud support**: Extend the service to back up to other cloud providers such as AWS S3 and Azure Blob Storage.
- **File encryption**: Implement encryption for files being backed up for added security.


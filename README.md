# 🚀 Automated Serverless API Deployment Pipeline

Welcome to my DevOps portfolio project! This repository contains the source code and infrastructure configurations for a fully automated, cloud-native serverless application deployed on Microsoft Azure.

## 📝 Project Overview
The goal of this project is to demonstrate end-to-end automation of cloud infrastructure and application deployment. Instead of manually provisioning resources via the Azure Portal, this project utilizes **Infrastructure as Code (IaC)** to build the environment and a **CI/CD Pipeline** to deploy the application logic.

## 🛠️ Tech Stack
* **Cloud Provider:** Microsoft Azure
* **Infrastructure as Code:** Terraform
* **Application Logic:** Python 3.11 (Azure Functions)
* **CI/CD Automation:** GitHub Actions
* **Version Control:** Git & GitHub

## 🏗️ Architecture & Workflow
1. **Developer Push:** Code is written locally and pushed to the `main` branch of this repository.
2. **GitHub Actions Trigger:** The push event automatically triggers the CI/CD pipeline (`deploy.yml`).
3. **Infrastructure Provisioning (Terraform):** The pipeline authenticates with Azure and runs `terraform apply` to ensure the required resources (Resource Group, Storage Account, App Service Plan, and Function App) exist and are properly configured.
4. **Application Deployment:** Once the infrastructure is ready, the pipeline packages the Python code and deploys it directly to the Azure Function App.
5. **Live API:** The Serverless API becomes immediately available via a public HTTP endpoint.

## 📂 Folder Structure
```text
.
├── .github/workflows/
│   └── deploy.yml         # GitHub Actions CI/CD Pipeline configuration
├── api/
│   ├── function_app.py    # Python logic for the Serverless API
│   └── requirements.txt   # Python dependencies
└── terraform/
    ├── main.tf            # Azure resource definitions
    └── provider.tf        # Terraform Azure provider setup

#### Sonata RAG Management System

### Problem Statement

Organizations face challenges in deploying scalable and reliable Retrieval-Augmented Generation (RAG) systems that seamlessly integrate large language models (LLMs) with external data sources to provide accurate, context-aware responses.

### Proposed Solution

The Sonata RAG Management System is a comprehensive platform designed to facilitate the deployment and management of production-grade RAG applications, ensuring scalability, reliability, and efficiency.

**Tech Stack**

1. Python: Primary language offering extensive AI and machine learning libraries.
2. Flask: Lightweight web framework for building scalable APIs.
3. Azure OpenAI: Access to advanced language models for generating human-like text responses.
4. Docker: Containerization for consistent development and deployment environments.
5. LangSmith: Platform for debugging, testing, evaluating, and monitoring LLM applications, ensuring robustness in production. 

**Infrastructure**

1. AWS S3: Scalable object storage for managing large datasets.
2. Azure App Service: Managed platform for deploying and scaling Flask web applications, integrating seamlessly with Azure OpenAI services.
3. GitHub Actions: CI/CD pipelines to automate testing and deployment, enhancing development efficiency.
4. Terraform: Infrastructure as code for consistent provisioning and management of cloud resources across AWS and Azure.

By integrating these technologies and infrastructure components, the Sonata RAG Management System aims to streamline the deployment and management of RAG applications, addressing scalability and reliability challenges effectively.

## Project Archietecture
![arch tech diagram](https://github.com/user-attachments/assets/6089e601-045e-4267-a7fd-755ac8ec2867)

## UI of the App

<img width="855" alt="image" src="https://github.com/user-attachments/assets/d19f8849-de87-44d2-ad9d-482e34b946ff" />

### Running in Docker Desktop
<img width="945" alt="image" src="https://github.com/user-attachments/assets/d5a71dc1-6d0b-48fa-8f2b-cd80216f0f0a" />



# How to run?

### STEPS:


### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n llmapp python=3.11 -y
```

```bash
conda activate llmapp
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python src/main.py
```


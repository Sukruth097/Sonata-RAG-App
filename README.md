Sonata RAG Management System

### Problem Statement

Organizations face challenges in deploying scalable and reliable Retrieval-Augmented Generation (RAG) systems that seamlessly integrate large language models (LLMs) with external data sources to provide accurate, context-aware responses.

### Proposed Solution

The Sonata RAG Management System is a comprehensive platform designed to facilitate the deployment and management of production-grade RAG applications, ensuring scalability, reliability, and efficiency.

- Tech Stack

Python: Primary language offering extensive AI and machine learning libraries.
Flask: Lightweight web framework for building scalable APIs.
Azure OpenAI: Access to advanced language models for generating human-like text responses.
Docker: Containerization for consistent development and deployment environments.
LangSmith: Platform for debugging, testing, evaluating, and monitoring LLM applications, ensuring robustness in production. 

- Infrastructure

AWS S3: Scalable object storage for managing large datasets.
Azure App Service: Managed platform for deploying and scaling Flask web applications, integrating seamlessly with Azure OpenAI services.
GitHub Actions: CI/CD pipelines to automate testing and deployment, enhancing development efficiency.
Terraform: Infrastructure as code for consistent provisioning and management of cloud resources across AWS and Azure.
By integrating these technologies and infrastructure components, the Sonata RAG Management System aims to streamline the deployment and management of RAG applications, addressing scalability and reliability challenges effectively.

## Project Archietecture
![image](https://github.com/user-attachments/assets/844476aa-f70f-49e2-b1f6-f53b56f22c21)


## UI of the App

<img width="855" alt="image" src="https://github.com/user-attachments/assets/d19f8849-de87-44d2-ad9d-482e34b946ff" />


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
python app/main.py
```

Now,
```bash
open up you local host and port
```

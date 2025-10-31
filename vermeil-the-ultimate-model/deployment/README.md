# Deployment

This directory contains everything needed to deploy the Vermeil model in a production environment. The goal is to provide a complete solution for serving the model as a scalable and reliable API, with support for containerization and CI/CD.

## Directory Structure

-   **`api/`**: This subdirectory contains the source code for the model's API. This could be a simple Flask or FastAPI server that exposes a single endpoint for running inference with the model.

-   **`ci_cd/`**: This subdirectory contains configuration files for continuous integration and continuous deployment (CI/CD) pipelines. These pipelines can be used to automate the process of testing, building, and deploying the model.

-   **`docker/`**: This subdirectory contains Dockerfiles and Docker Compose files for containerizing the model serving component. Containerization makes it easy to package the model serving component and its dependencies into a single, portable unit that can be run in any environment.

-   **`fastapi_app/`**: This subdirectory contains a more complete FastAPI server for serving the model. It may include features like request validation, authentication, and interactive API documentation.

-   **`gradio_ui/`**: This subdirectory contains a Gradio interface for creating an interactive demo of the model. This is a great way to showcase the model's capabilities to a wider audience.

## Deployment Strategy

The recommended deployment strategy is as follows:

1.  **Containerize the model serving component**: Use the Dockerfile in `docker/` to build a Docker image of the model server.
2.  **Push the image to a container registry**: Push the Docker image to a container registry like Docker Hub, Amazon ECR, or Google Container Registry.
3.  **Deploy the image to a cloud service**: Deploy the Docker image to a cloud service that supports container orchestration, such as Amazon ECS, Google Kubernetes Engine (GKE), or Microsoft Azure Kubernetes Service (AKS).
4.  **Set up a CI/CD pipeline**: Use the CI/CD pipeline in `ci_cd/` to automate the process of building and deploying the model whenever new code is pushed to the repository.

## Local Deployment

For local testing and development, you can use Docker Compose to run the model serving component locally.

```bash
# Build and run the model serving component using Docker Compose
docker-compose -f deployment/docker/compose.yaml up --build
```

This will start the FastAPI server and make it available at `http://localhost:8000`.
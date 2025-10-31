# Docker

This directory contains the Docker-related files for the Vermeil project. Docker is a containerization platform that allows you to package the model serving component and its dependencies into a single, portable unit called a Docker image. This makes it easy to deploy and run the model server in any environment, from a local machine to a cloud server.

## Files

-   **`Dockerfile`**: This file contains the instructions for building a Docker image for serving the Vermeil model. The Dockerfile specifies:
    -   The base image to use (e.g., a Python image).
    -   The dependencies to install.
    -   The source code to copy into the image.
    -   The command to run when the container is started.

-   **`compose.yaml`**: This file is a Docker Compose file that defines a multi-container Docker setup. It can be used to run the Vermeil model server and its dependencies (e.g., a database, a message queue) with a single command. The `compose.yaml` file specifies:
    -   The services to run (e.g., the API, a database).
    -   The Docker image to use for each service.
    -   The ports to expose.
    -   The volumes to mount.

## Building the Docker Image

To build the Docker image, you can use the `docker build` command:

```bash
# Build the Docker image
docker build -t vermeil:latest -f deployment/docker/Dockerfile .
```

This will build a Docker image with the tag `vermeil:latest`.

## Running the Model Server with Docker Compose

To run the model server using Docker Compose, you can use the `docker-compose` command:

```bash
# Run the model server in the background
docker-compose -f deployment/docker/compose.yaml up -d

# Stop the model server
docker-compose -f deployment/docker/compose.yaml down
```

This will start the Vermeil model server and any other services defined in the `compose.yaml` file.

## Benefits of Using Docker

-   **Portability**: A Docker image can be run on any machine that has Docker installed, regardless of the underlying operating system.
-   **Reproducibility**: A Docker image captures the exact environment that the model server needs to run, ensuring that the model server behaves the same way every time.
-   **Isolation**: Docker containers provide a high degree of isolation, which can improve security and prevent conflicts between different services.
-   **Scalability**: Docker makes it easy to scale a service by running multiple instances of the same container.

By using Docker, we can simplify the deployment process and make the Vermeil project more robust and reliable.
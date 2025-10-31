# API

This directory contains the source code for the Vermeil model's API. The API is responsible for exposing the model's functionality to the outside world, allowing users and other services to interact with the model through a simple and consistent interface.

## Directory Structure

-   **`_files/app.py`**: This file contains the main logic for the API. It is responsible for:
    -   Loading the trained model.
    -   Defining the API endpoints.
    -   Handling incoming requests.
    -   Running inference with the model.
    -   Returning the model's predictions.

-   **`routes/`**: This subdirectory contains the API routes for the different modalities. Each file in this directory defines the routes for a specific modality (e.g., `text.py`, `image.py`, `multimodal.py`). This helps to keep the API organized and easy to maintain.

## API Framework

We use [FastAPI](https://fastapi.tiangolo.com/) as the framework for our API. FastAPI is a modern, high-performance web framework for building APIs with Python. It offers several advantages, including:

-   **High performance**: FastAPI is one of the fastest Python web frameworks available.
-   **Automatic documentation**: FastAPI automatically generates interactive API documentation (using Swagger UI and ReDoc).
-   **Type hints and validation**: FastAPI uses Python type hints to validate incoming requests and to provide autocompletion in the editor.
-   **Asynchronous support**: FastAPI supports asynchronous request handling, which can improve performance for I/O-bound tasks.

## Running the API

To run the API locally, you can use a web server like [Uvicorn](https://www.uvicorn.org/).

```bash
# Run the API using Uvicorn
uvicorn deployment.api._files.app:app --reload
```

This will start the API server and make it available at `http://localhost:8000`. You can then access the interactive API documentation at `http://localhost:8000/docs`.

## API Endpoints

The API exposes a set of endpoints for interacting with the model. For example, the `text.py` route might define the following endpoints:

-   `POST /text/generate`: Generate text from a given prompt.
-   `POST /text/classify`: Classify a given text into a set of categories.

Each endpoint has a well-defined request and response format, which is documented in the interactive API documentation.

## Extending the API

To add a new endpoint to the API, you can:

1.  Add a new function to the appropriate route file in the `routes/` directory.
2.  Decorate the function with the appropriate FastAPI decorator (e.g., `@app.post("/my-new-endpoint")`).
3.  Define the request and response format using Pydantic models.
4.  Implement the logic for handling the request and returning the response.
# FastAPI Project

## Description

This project is a simple FastAPI application that verifies an OAuth token and processes user input with five parameters. The parameters are slightly modified before being returned in the response.

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the FastAPI application:
    ```bash
    uvicorn app:app --reload
    ```

3. Send a POST request to `/process` with the following JSON body:
    ```json
    {
        "param1": "string",
        "param2": 123,
        "param3": 1.23,
        "param4": true,
        "param5": "string"
    }
    ```

4. Include an OAuth token in the `Authorization` header:
    ```bash
    Authorization: your-secret-token
    ```

## Configuration

The OAuth token is configured in `config.yaml`. Change the token value to match the one you use.

## Documentation

See `Projectdocumentation.docx` for detailed project documentation.

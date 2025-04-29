# NexConnect
A low-code/no-code data integration platform built with FastAPI.



## Setting Up the Development Environment

To set up the development environment, follow these steps:
 
### Create a Virtual Environment

1. Navigate to the project directory:
    ```sh
    cd /E:/Python/FinPlay Academy/Game Backend
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

### Install Dependencies

With the virtual environment activated, install the required dependencies:
```sh
pip install -r requirements.txt
```

### Run the Project

To run the FastAPI application, execute the following command:
```sh
uvicorn app.main:app --reload
```

This will start the development server and you can access the API documentation at `http://127.0.0.1:8000/docs`.
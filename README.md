# Elikiba Backend

This repository contains the backend code for the Elikiba project, built using the Flask web framework.

## Project Setup

1. Prerequisites:
        Ensure you have Python (version 3.6 or later) and pip (the package installer) installed on your system. You can verify this by running python --version and pip --version in your terminal. If not installed, download them from https://www.python.org/downloads/.
2. Create a virtual environment (recommended):
    - Virtual environments isolate project dependencies, preventing conflicts with other projects. To create one, use the following command (replace myvenv with your desired environment name):
    ```sh
        python -m virtualenv venv
    ```

    - Activate the virtual environment:
        - Windows: venv\Scripts\activate
        - macOS/Linux: source venv/bin/activate

3. Install dependencies:
    - Within the activated virtual environment, install the required dependencies listed in `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

## Running the Application
### Launch the development server:
- After installing dependencies, start the fastapi development server by running:
    ```sh
    uvicorn main:app --reload
    ```

    This will typically start the server on http://127.0.0.1:5000/ (localhost, port 5000). You can access your application in your web browser at that URL.


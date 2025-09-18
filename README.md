# Sewer Inspection AI Chat Agent

This project provides an AI chat agent to query sewer inspection data using natural language. It features a FastAPI backend powered by Langchain's Pandas DataFrame Agent and Ollama, and a React TypeScript frontend for interactive chat.

## Project Structure

- `data/`: Contains the `sewer-inspections-part1.jsonl` data file.
- `sewerai_assessment/`: Backend Python application.
    - `data_processor.py`: Handles loading and sampling the raw JSONL data into a Pandas DataFrame.
    - `agent.py`: Contains the Langchain Pandas DataFrame Agent responsible for processing natural language queries.
    - `main.py`: The FastAPI application that serves as the API endpoint for the chat agent.
- `frontend/`: React + TypeScript frontend application.
    - Implements the user interface for the chat agent.
- `requirements.txt`: Lists all Python dependencies for the backend.
- `package.json` (in `frontend/`): Lists all Node.js dependencies for the frontend.
- `screenshot.jpg`: A visual representation of the application.

## Features

- **Natural Language Querying**: Ask questions about sewer inspection data in plain English.
- **Pandas DataFrame Integration**: Leverages Langchain's Pandas DataFrame Agent to query structured data.
- **Ollama Integration**: Uses Ollama (with the Llama3 model) for local embedding and language model processing, ensuring data privacy and offline capability.
- **FastAPI Backend**: A robust and asynchronous API to serve queries from the frontend.
- **React + TypeScript Frontend**: A modern, interactive web interface for the chat agent.
- **Data Sampling**: The application samples 10% of the original data for faster development and validation.

## How to Run the Project

Follow these steps to set up and run both the backend and frontend components.

### Prerequisites

1.  **Python 3.8+ and `pip`**: Ensure Python and its package installer are set up.
2.  **Node.js and `npm`**: Ensure Node.js and npm are installed for the frontend.
3.  **Ollama**: Install Ollama from [ollama.com](https://ollama.com/).
4.  **Llama3 Model**: Pull the `llama3` model using Ollama:
    ```bash
    ollama pull llama3
    ```
5.  **Virtual Environment (Recommended)**: Activate your virtual environment: `source ~/.venv/venv/bin/activate`

### 1. Start the Ollama Server

In a *separate* terminal, start the Ollama server:

```bash
ollama serve
```
Keep this terminal running in the background.

### 2. Set up and Run the Backend (FastAPI)

From the project root directory (`sewerai_assessment/`):

1.  **Install Python dependencies**:
    ```bash
    source ~/.venv/venv/bin/activate && pip install -r requirements.txt
    ```
2.  **Run the FastAPI application**:
    ```bash
    source ~/.venv/venv/bin/activate && python -m sewerai_assessment.main
    ```
    This will start the backend server, typically on `http://localhost:8000`. Keep this terminal running.

### 3. Set up and Run the Frontend (React)

From the project root directory:

1.  **Navigate to the frontend directory**:
    ```bash
    cd frontend
    ```
2.  **Install Node.js dependencies**:
    ```bash
    npm install
    ```
3.  **Start the React development server**:
    ```bash
    npm run dev
    ```
    This will start the frontend development server, typically on `http://localhost:5173/`. Keep this terminal running.

### 4. Access the Application

Open your web browser and navigate to `http://localhost:5173/`. You should see the chat interface ready to accept your queries.

## Screenshot

Here's a screenshot of the chat agent:

![Screenshot of the Sewer Inspection AI Chat Agent](screenshot.jpg)

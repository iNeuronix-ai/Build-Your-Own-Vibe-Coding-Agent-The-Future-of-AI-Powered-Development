# Vibe Coding Agent - Setup Guide

## Introduction
Vibe Coding Agent is a FastAPI-based application that integrates with Google Gemini to generate Python code from speech input. This guide provides step-by-step installation and setup instructions for both Anaconda and standard Python virtual environments.

---

## Prerequisites
Ensure you have the following installed on your system:

- Python (>=3.8)
- Anaconda (if using Conda virtual environment)
- pip (Python package manager)

### Required Python Packages
The following dependencies are required and will be installed via `requirements.txt`:
- `fastapi`
- `uvicorn`
- `phidata`
- `google-generativeai`

---

## Setup using Python Virtual Environment

### Step 1: Clone the Repository
```sh
git clone https://github.com/iNeuronix-ai/Build-Your-Own-Vibe-Coding-Agent-The-Future-of-AI-Powered-Development-.git
cd <repository_name> Build-Your-Own-Vibe-Coding-Agent-The-Future-of-AI-Powered-Development-
```

### Step 2: Create and Activate Virtual Environment
#### For Windows:
```sh
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Set Environment Variable for Google API Key
Replace `<YOUR_GOOGLE_API_KEY>` with your actual API key.

#### For Windows (Command Prompt):
```sh
set GOOGLE_API_KEY=<YOUR_GOOGLE_API_KEY>
```

#### For Windows (PowerShell):
```sh
$env:GOOGLE_API_KEY="<YOUR_GOOGLE_API_KEY>"
```

#### For macOS/Linux:
```sh
export GOOGLE_API_KEY=<YOUR_GOOGLE_API_KEY>
```

### Step 5: Run the FastAPI Server
```sh
uvicorn agent:app  --port 3000 --reload
```

---

## Setup using Anaconda Virtual Environment

### Step 1: Clone the Repository
```sh
git clone https://github.com/iNeuronix-ai/Build-Your-Own-Vibe-Coding-Agent-The-Future-of-AI-Powered-Development-.git
cd <repository_name> Build-Your-Own-Vibe-Coding-Agent-The-Future-of-AI-Powered-Development-
```

### Step 2: Create and Activate Conda Environment
```sh
conda create --name vibe_env python=3.8 -y
conda activate vibe_env
```

### Step 3: Install Required Dependencies
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Set Environment Variable for Google API Key
Replace `<YOUR_GOOGLE_API_KEY>` with your actual API key.

#### For Windows (Anaconda Prompt):
```sh
set GOOGLE_API_KEY=<YOUR_GOOGLE_API_KEY>
```

#### For macOS/Linux:
```sh
export GOOGLE_API_KEY=<YOUR_GOOGLE_API_KEY>
```

### Step 5: Run the FastAPI Server
```sh
uvicorn agent:app --host 0.0.0.0 --port 8000 --reload
```

---

## API Endpoints
### 1. Generate Code from Speech Input
- **Endpoint:** `POST /generate_code`
- **Payload Format:**
```json
{
  "text": "your voice-transcribed text here"
}
```
- **Response:**
```json
{
  "message": "Code generated successfully"
}
```

### 2. Fetch Latest Generated Code
- **Endpoint:** `GET /latest_code`
- **Response:**
```json
{
  "filename": "latest_file.py",
  "content": "print('Hello World')"
}
```

### 3. Serve the UI
- **Endpoint:** `GET /`
- **Description:** Serves `static/index.html`

---

## Additional Notes
- Ensure your API key is valid to avoid authentication issues.
- Use `CTRL+C` to stop the FastAPI server.
- You can update dependencies using `pip install --upgrade -r requirements.txt`.

---

## License
This project is open-source and available under the MIT License.

Happy coding!


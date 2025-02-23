from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from phi.agent import Agent
from phi.tools.python import PythonTools
from phi.model.google import Gemini
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Set Google API Key
os.environ['GOOGLE_API_KEY'] = "AIzaSyBDb3hK3_6UWZX0CekzyWepWGSXWtnBJvM"  # Replace with your actual key

# Initialize FastAPI app
app = FastAPI()

# Allow frontend requests (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (Frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Phi Agent with Gemini 1.5 Flash
agent = Agent(model=Gemini(id="gemini-1.5-flash"), tools=[PythonTools()], show_tool_calls=True,save_and_run=True)

# Request model for API
class SpeechInput(BaseModel):
    text: str

# Function to get the latest Python file
def get_latest_python_file():
    python_files = glob.glob("*.py")  # Get all .py files in the directory
    if not python_files:
        return None
    latest_file = max(python_files, key=os.path.getctime)  # Get most recently created file
    return latest_file

# Route to process speech and generate code
@app.post("/generate_code")
async def generate_code(speech: SpeechInput):
    print(f"User said: {speech.text}")  # Debugging

    # Generate response from Phi Agent
    response = agent.print_response(speech.text)

    return {"message": "Code generated successfully"}

# Route to get the latest Python file content
@app.get("/latest_code")
async def latest_code():
    latest_file = get_latest_python_file()
    if not latest_file:
        return JSONResponse(content={"error": "No Python files found"}, status_code=404)

    with open(latest_file, "r") as f:
        code_content = f.read()

    return {"filename": latest_file, "content": code_content}

# Route to serve UI (index.html)
@app.get("/")
async def serve_ui():
    return FileResponse("static/index.html")

# Run FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

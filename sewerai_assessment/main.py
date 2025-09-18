from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware # Added CORS import
from pydantic import BaseModel
import uvicorn
import pandas as pd
from contextlib import asynccontextmanager

from sewerai_assessment.data_processor import load_all_jsonl_data
from sewerai_assessment.agent import create_dataframe_agent

app = FastAPI()

# Added CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Allow frontend origin
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods (GET, POST, etc.)
    allow_headers=["*"], # Allow all headers
)

class QueryRequest(BaseModel):
    query: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load and sample data once on startup
    df = load_all_jsonl_data('./data/')
    app.state.sampled_df = df.sample(frac=0.1, random_state=42)
    print(f"Sampled down to {len(app.state.sampled_df)} records (10% of original) for API use.")
    
    # Initialize the agent once on startup
    print("Initializing Pandas DataFrame Agent for API. Ensure Ollama server is running and 'llama3' model is pulled.")
    app.state.agent = create_dataframe_agent(app.state.sampled_df)
    print("Pandas DataFrame Agent initialized for API.")
    yield

@app.post("/query")
async def query_data(request: QueryRequest):
    try:
        response = app.state.agent.invoke({"input": request.query}) # Changed .run to .invoke
        return {"response": response.get('output', str(response))} # Handle potential missing 'output' key
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

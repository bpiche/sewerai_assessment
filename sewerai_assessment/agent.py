import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.llms import Ollama
from sewerai_assessment.data_processor import load_jsonl_data
import os

def create_dataframe_agent(df):
    # Initialize Ollama LLM
    # Ensure Ollama server is running and `llama3` model is pulled (e.g., `ollama pull llama3`)
    llm = Ollama(model="llama3") 
    agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)
    return agent

if __name__ == '__main__':
    # Load and sample data
    file_path = './data/sewer-inspections-part1.jsonl'
    df = load_jsonl_data(file_path)
    
    # Sample 10% of the DataFrame for quicker validation
    sampled_df = df.sample(frac=0.1, random_state=42)
    print(f"Sampled down to {len(sampled_df)} records (10% of original) for quicker validation.")

    # Create the agent
    print("\nAttempting to create Pandas DataFrame Agent using Ollama and Llama3.")
    print("Please ensure Ollama server is running and 'llama3' model is pulled (e.g., run 'ollama pull llama3' in your terminal).")
    print("If you encounter connection errors, verify your Ollama server is accessible.")

    agent = create_dataframe_agent(sampled_df)

    # Example query
    query = "What inspections required repair in Sacramento, California?"
    print(f"\nQuerying: {query}")
    response = agent.run(query)
    print("\nResponse:")
    print(response)

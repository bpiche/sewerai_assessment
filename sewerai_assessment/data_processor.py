import pandas as pd
import json
import os
from tqdm import tqdm

def load_jsonl_data(file_path):
    print(f"Loading data from {file_path}...")
    data = []
    with open(file_path, 'r') as f:
        for line in tqdm(f, desc="Loading JSONL lines"):
            data.append(json.loads(line))
    df = pd.DataFrame(data)
    print(f"Finished loading {len(df)} records.")
    return df

if __name__ == '__main__':
    file_path = './data/sewer-inspections-part1.jsonl'
    df = load_jsonl_data(file_path)
    print(df.head())
    print(f"Loaded {len(df)} records.")

    # Sample 10% of the DataFrame for quicker validation
    sampled_df = df.sample(frac=0.1, random_state=42)
    print(f"Sampled down to {len(sampled_df)} records (10% of original) for quicker validation.")
    print("Data loading and sampling complete.")

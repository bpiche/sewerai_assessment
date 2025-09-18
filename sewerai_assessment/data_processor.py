import pandas as pd
import json
import os
import urllib.request
import s3fs # Import s3fs for pandas to directly read from s3
from tqdm import tqdm

S3_BUCKET_NAME = "sewerai-public"
DATA_DIR = "./data/"

def download_s3_file(bucket_name, s3_key, local_path):
    if os.path.exists(local_path):
        print(f"File already exists locally: {local_path}")
        return

    print(f"Downloading s3://{bucket_name}/{s3_key} to {local_path}...")
    s3_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"
    try:
        urllib.request.urlretrieve(s3_url, local_path)
        print(f"Successfully downloaded {s3_key}")
    except Exception as e:
        print(f"Error downloading {s3_key} from {s3_url}: {e}")

def load_all_jsonl_data(data_dir):
    all_data = []
    file_numbers = range(1, 6) # part1.jsonl to part5.jsonl

    os.makedirs(data_dir, exist_ok=True)

    for i in file_numbers:
        file_name = f"sewer-inspections-part{i}.jsonl"
        s3_key = file_name
        local_file_path = os.path.join(data_dir, file_name)
        
        # Attempt to download the file if it's not present locally
        # Note: For this to work, the bucket 'sewerai-public' must be publicly readable.
        # If it's private, AWS credentials must be configured in the environment.
        download_s3_file(S3_BUCKET_NAME, s3_key, local_file_path)

        if os.path.exists(local_file_path):
            print(f"Loading data from {local_file_path}...")
            with open(local_file_path, 'r') as f:
                # Assuming this runs relatively quickly due to smaller file sizes per part
                for line in tqdm(f, desc=f"Loading {file_name}"):
                    all_data.append(json.loads(line))
        else:
            print(f"Skipping {file_name}: file not found locally and could not be downloaded.")

    df = pd.DataFrame(all_data)
    print(f"Finished loading a total of {len(df)} records from all files.")
    return df

if __name__ == '__main__':
    df = load_all_jsonl_data(DATA_DIR)
    print(df.head())
    print(f"Loaded {len(df)} records.")

    # Sample 10% of the DataFrame for quicker validation
    sampled_df = df.sample(frac=0.1, random_state=42)
    print(f"Sampled down to {len(sampled_df)} records (10% of original) for quicker validation.")
    print("Data loading and sampling complete.")

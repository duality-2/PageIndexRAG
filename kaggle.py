import kagglehub
import os

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# Download latest version to data/ directory
path = kagglehub.dataset_download("hhs/health-insurance-marketplace", path="data")

print("Path to dataset files:", path)

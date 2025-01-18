import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY not found. Please check your .env file.")

# Example usage
print(f"Your API Key is: {api_key}")
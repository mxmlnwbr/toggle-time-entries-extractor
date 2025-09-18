import os
import requests
import json
from base64 import b64encode
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

def main():
    data = requests.get('https://api.track.toggl.com/api/v9/me/time_entries', headers={'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(f"{API_TOKEN}:api_token".encode("ascii")).decode("ascii")})
    
    os.makedirs("data", exist_ok=True)
    with open("data/time_entries.json", "w") as f:
        for time_entry in data.json():
            f.write(json.dumps(time_entry) + "\n")

    print("Time entries extracted successfully!")


if __name__ == "__main__":
    main()

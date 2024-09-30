import requests
import os
from src.utils import get_env_value

# Load environment variables from the .env file
APIKEY = get_env_value("APIKEY")
if APIKEY is None :
    raise Exception("No api key found")

def get_data():
    """sending a request to the api and return the data"""

    url = f"https://api.freecurrencyapi.com/v1/latest"
    params = {"apikey": APIKEY}
    headers = {}
    response = requests.request("GET", url, headers=headers, params=params)
    if response.status_code == 200:
        return response
    else :
        print(f"Something went wrong:\n{response}")
        print(response.text)
        return None

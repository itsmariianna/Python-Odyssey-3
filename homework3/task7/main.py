import requests

def get_invalid_url():
    url = "https://jsonplaceholder.typicode.com/invalid-url"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Response received:", response.json())
    else:
        print(f"Request failed with status code {response.status_code}: {response.reason}")
        
get_invalid_url()

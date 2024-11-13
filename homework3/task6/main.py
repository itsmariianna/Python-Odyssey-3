import requests

def create_post(title, body, user_id):

    url = "https://jsonplaceholder.typicode.com/posts"
    
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    
    response = requests.post(url, json = data)
    
    if response.status_code == 201:
        successfully = response.json()
        print(f"Post has been created successfully -> {successfully}")
    else:
        print(f"Failed to create post: {response.status_code}")


create_post("My Title", "Body text here", 2)

import requests

def get_user_posts(user_id):

    url = f"https://jsonplaceholder.typicode.com/posts"
    params = {'userId': user_id}

    response = requests.get(url, params = params)

    if response.status_code == 200:
        data = response.json()

        print(f'All titles for this userID = {user_id}')
        for i in data:
            print(i["title"])

    else:
        print(f"Failed to retrieve data: {response.status_code}")\
        

get_user_posts(2)
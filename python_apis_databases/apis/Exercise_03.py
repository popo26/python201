'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests

url = "http://demo.codingnomads.co:8080/tasks_api/users"

new_user = {
    "email": "ai@awesome.com",
    "first_name": "Ai",
    "last_name": "Oakenfull",
}

response = requests.post(url, json=new_user)

print(response)
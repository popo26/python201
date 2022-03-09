'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests

id = 151
url = f"http://demo.codingnomads.co:8080/tasks_api/users/{id}" #one way to add id with f string. The other way to add by [response = requests.put(url + "/151", json=edit_user)]

edit_user = {
    "email": "ai4@awesome.com",
    "first_name": "Ai",
    "last_name": "Oakenfull",
}

response = requests.put(url, json=edit_user)
print(response)

# response = requests.post(url, json=new_user)
# print(response)
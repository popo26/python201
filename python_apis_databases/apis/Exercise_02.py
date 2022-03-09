'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
import requests

URL = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(URL)

email_list = []
data = response.json()
data2= data["data"]

for item in data2:
    for key in item:
        if key == "email":
            email_list.append(item["email"])
print(email_list)

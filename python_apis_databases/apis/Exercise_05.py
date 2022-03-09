'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''

import requests

id=154
url = f"http://demo.codingnomads.co:8080/tasks_api/users/{id}" # Again same as PUT, instead[requests.delete(url + /154)] works as well.

response = requests.delete(url)
print(response)
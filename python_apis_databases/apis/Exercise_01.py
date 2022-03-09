'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body



'''
import requests

URL = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(URL)
print(f'Status code is {response}')
print(f'Encoding of the response is {response.encoding}')
print(f'text of the response body is {response.text}')
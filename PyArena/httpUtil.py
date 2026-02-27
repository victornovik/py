import requests

# print(requests.__file__)

req = requests.get('https://www.python.org')
print(req.text)
print(req.status_code)

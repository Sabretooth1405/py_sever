import requests
response = requests.get("http://192.168.1.39:8000/")
print(response.headers)
#print(response.text)

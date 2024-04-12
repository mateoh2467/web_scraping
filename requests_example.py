import requests

server_requests = requests.get("https://www.google.com")
status_code = server_requests.status_code
print(status_code)

if (status_code == 200):
    print("you have connected")
else:
    print("you have not connected")
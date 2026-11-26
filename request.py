import requests


url = 'http://localhost:8000'
packet = {"Hey there solomon this is a test packet"}
x = requests.post(url, json = packet)
print(x.text)
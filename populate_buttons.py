import requests
import random
import os


data = list()
os.environ['NO_PROXY'] = '127.0.0.1'
for i in range(100):
    for j in range(3):
        body = {
        "name": f"B{i}",
        "click_type": j,
        "battery": random.randrange(1,100),
        "location": 1
        }
        req = requests.post('http://localhost:8000/api/button/', data = body)
        print(req.text)

print(data)
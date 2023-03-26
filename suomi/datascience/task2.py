""" Task2: playing with the requests """
import requests
import json


r = requests.post("https://api.sentino.org/api/score/text",
                  headers={'Authorization': 'Token 0df3b4f908b73cd3db94914e1df768f79f9331e0'},
                  json={"text": "I do not know who I am", "inventories": ["big5", "neo"]},
                  )
data = json.loads(r.text)
print(data)

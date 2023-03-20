from suomi import greets
import requests

greets('World')

r = requests.post("https://api.sentino.org/api/score/text",
  headers={'Authorization': 'Token 0df3b4f908b73cd3db94914e1df768f79f9331e0'},
  json={"text": "I am extraverted", "inventories": ["big5", "neo"]},
)

print("results:", r.json())

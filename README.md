# Suomi package
A test package made for spending time coding and commiting! **Yay**!

*18.03.2023*: only one function is included: try **greet()** after installing the package

## Setup
```pip install -e .```

## Usage

Usage of the greets function:
```
from suomi import greets

greets('stranger')
#greets()

```

Usage of the API requests:
```
import requests

r = requests.post("https://api.sentino.org/api/score/text",
                  headers={'Authorization': 'Token 0df3b4f908b73cd3db94914e1df768f79f9331e0'},
                  json={"text": "YOUR TEXT HERE", "inventories": ["big5", "neo"]},
                  )
```

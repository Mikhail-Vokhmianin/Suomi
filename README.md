# Suomi package
A test package made for spending time coding and commiting! **Yay**!

*18.03.2023*: only one function is included: try **greets()** after installing the package
*01.04.2023*: another function is added: try **text_analysis**

## Setup
```pip install -e .```

## Tests
Run ``` pytest``` to validate package performance.

You can also check this for different python version (specified in the **tox.ini**)
using the  **tox** package and running the same ```tox``` command (note that the
corresponding python versions should be installed on your machine).

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

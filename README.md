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

### Usage of the greets function:
```
from suomi import greets

greets('stranger')
#greets()

```

### Usage of the API requests:
```
import requests

r = requests.post("https://api.sentino.org/api/score/text",
                  headers={'Authorization': 'YOUR TOKEN'},
                  json={"text": "YOUR TEXT", "inventories": ["big5", "neo"]},
                  )
```

### Usage of the text_analysis
Results are obtained for the [big5 personalty test](https://en.wikipedia.org/wiki/Big_Five_personality_traits) on defalut,
this example show usage for the [NEO personality test](https://en.wikipedia.org/wiki/Revised_NEO_Personality_Inventory):
```
from suomi import text_analysis

result = text_analysis('I like to be tested','neo')
```

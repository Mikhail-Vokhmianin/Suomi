""" Task2: playing with Sentino API """

__version__ = '0.1.1'

import requests
import json
import pandas as pd


def sentino_test_results(your_text, test_name='big5'):
    """ Analyze your text using API request from Sentino

    Parameters
    ----------
    your_text: string
    test_name: string

    Return
    ---------
    psychological portrait: DataFrame
    """
    if not isinstance(your_text, str) or len(your_text) == 0:
        raise TypeError('First argument should be a text with at least 1 character')
    else:
        r = requests.post("https://api.sentino.org/api/score/text",
                          headers={'Authorization': 'Token 0df3b4f908b73cd3db94914e1df768f79f9331e0'},
                          json={"text": your_text, "inventories": [test_name]},
                          )
        data = json.loads(r.text)

        lab = [str(key).capitalize() for key in data['scoring'][test_name].keys()]
        quan = [data['scoring'][test_name][key]['quantile'] for key in data['scoring'][test_name]]
        sc = [data['scoring'][test_name][key]['score'] for key in data['scoring'][test_name]]
        conf = [data['scoring'][test_name][key]['confidence'] for key in data['scoring'][test_name]]
        conf_text = [data['scoring'][test_name][key]['confidence_text'] for key in data['scoring'][test_name]]

        surprise = pd.DataFrame({'labels': lab,
                                 'quantiles': quan,
                                 'score': sc,
                                 'confidence': conf,
                                 'confidence_text': conf_text,
                                 })

    return surprise

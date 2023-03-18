from suomi import greets
import requests

greets('World')

textdata = requests.get(API)

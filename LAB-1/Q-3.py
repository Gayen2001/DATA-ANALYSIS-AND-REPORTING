# WAPP to use response json() to print formatted string
import pprint
import requests

urlName = 'https://api.restful-api.dev/objects'

responce= requests.get(urlName)

pprint.pprint(respone.json())

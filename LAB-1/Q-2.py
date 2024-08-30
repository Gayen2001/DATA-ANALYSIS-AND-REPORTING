# WAPP to use response json() using Request
import requests
urlName='https://api.restful-api.dev/objects'
responce= requests.get(urlName)
print(responce.json())

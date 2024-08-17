# WAPP to Implement API Request using Get
import requests
response =requests.get("https://en.wikipedia.org/wiki/Turbo_(2024_film)")
print(response.status_code)
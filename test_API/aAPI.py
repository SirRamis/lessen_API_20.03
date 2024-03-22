import requests

response = requests.get('https://restful-booker.herokuapp.com/booking')

print(response.json())
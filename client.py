import requests

BASE_URL = 'host'
response = requests.get(BASE_URL + '/hello_get')
print('Server responded to get with: ', response.json())

data_sent = {'first_name': 'somevalue'}
response = requests.post(BASE_URL + '/hello_post', json=data_sent)
print('Server responded to POST with:', response.json())
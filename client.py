import requests

data_sent = {'first_name': 'somevalue'}
r = requests.post('http://10.188.143.81:5000', json=data_sent)
print('data received', r.json())
print("HEY")

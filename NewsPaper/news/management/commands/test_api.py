import requests

BASE_URL = 'http://localhost:8000/posts'

response = requests.get(f'{BASE_URL}/news/')
print('GET /news/ response:', response.status_code)
print('Response content:', response.json())

# data = {'title': 'Название поста', 'content': 'Содержимое поста'}
# response = requests.post(f'{BASE_URL}/news/', json=data)
# print('POST /news/ response:', response.status_code)
# print('Response content:', response.json())

# headers = {'Authorization': 'Token YOUR_TOKEN'}
# response = requests.post(f'{BASE_URL}/news/', json=data, headers=headers)
# print('POST /news/ with authentication response:', response.status_code)
# print('Response content:', response.json())

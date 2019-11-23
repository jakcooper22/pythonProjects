from redditTest2 import d, data
import requests

print(d)

token = 'bearer ' + d['access_token']

print(token)

base_url_oauth = 'https://oauth.reddit.com'

headers = {'Authorization': token, 'User-Agent': 'APP-NAME by REDDIT-USERNAME'}
response = requests.get(base_url_oauth + '/api/v1/me', headers=headers)

print(response)

if response.status_code == 200:
    print(response.json()['name'], response.json()['comment_karma'])
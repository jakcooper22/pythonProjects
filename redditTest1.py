import creds
import requests
import requests.auth

data = []

headers = {'User agent': 'Test Script by /u/ + \creds.uname'}

client_auth = requests.auth.HTTPBasicAuth(creds.CLIENT_ID, creds.CLIENT_SECRET)

post_data = {"grant_type": "password", 
             "username": creds.uname, "password": creds.pword}

response = requests.post("https://www.reddit.com/api/v1/access_token", 
                         auth=client_auth, data=post_data)

client = requests.session()
client.headers = headers

print(response)

r = client.get(r'http://www.reddit.com/user/ + \creds.uname')
r.text
# data = r.json()

# print(data['data']['children'][0])
print(data)
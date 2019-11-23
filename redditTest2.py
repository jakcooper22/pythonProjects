import requests
import creds

from __main__ import *

base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': creds.uname, 'password': creds.pword}
auth = requests.auth.HTTPBasicAuth(creds.CLIENT_ID, creds.CLIENT_SECRET)
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
		  auth=auth)
d = r.json()


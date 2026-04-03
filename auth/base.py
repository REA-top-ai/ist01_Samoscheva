import requests
from requests.auth import HTTPBasicAuth

url = 'https://httpbin.org/basic-auth/ist01_Samoscheva_VA/samoschevaV'
basic = HTTPBasicAuth('ist01_Samoscheva_VA', 'samoschevaV')
response = requests.get(url, auth=basic)

print(response)

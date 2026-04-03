import requests
from requests.auth import HTTPDigestAuth

url = 'https://httpbin.org/digest-auth/auth/ist01_Samoscheva_VA/samoschevaV'
basic = HTTPDigestAuth('ist01_Samoscheva_VA', 'samoschevaV')
response = requests.get(url, auth = basic)

print(response)
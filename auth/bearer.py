import requests

url = "https://httpbin.org/bearer"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJpc3QwMV9TYW1vc2NoZXZhX1ZBIiwibmFtZSI6InNhbW9zY2hldmFWIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.fvgtK7AAL3eqf7WIwjApDF6fHqRo5MMc_MwECElAfYQ"
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url, headers = headers)

print( response)

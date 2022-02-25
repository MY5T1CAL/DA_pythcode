import requests
url = 'https://192.168.230.130/photography/'
r = requests.get(url)
print(r.text)

print("status code: ")
print("\t", r.status_code)

h = requests.head(url)
print("Header: ")
print("************")
for photo in h.headers:
    print("\t", photo, ".", h.headers[photo])
print("************")
headers = {
    'User-Agent': 'Mobile'
}
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)

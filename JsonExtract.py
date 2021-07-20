import ssl
import urllib.request
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location:")
print("Retrieving",url)

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
count = 0
sum = 0
for element in js['comments']:
    sum = sum + element['count']
    count += 1
print('Count:',count)
print('Sum:',sum)

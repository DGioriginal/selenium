import requests
res = requests.get('https://google.com')
try:
    res.raise_for_status()
except:
    print('Find error: %s' % (exc))
playFile = open('Romeo.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
res.raise_for_status()
playFile.close()
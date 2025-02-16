import requests, webbrowser, bs4, pyperclip, sys
print('Search..')
pyper = pyperclip.paste()
res = requests.get('https://pypi.org/search/?q=' + ' '.join(pyper))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet') #<a class = 'package-snippet' href= '..'> где будем сыллку брать
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    webbrowser.open(urlToOpen)

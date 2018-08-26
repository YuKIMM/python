import requests


url = 'http://www.mmjpg.com/tag/xinggan/'

r = requests.get(url)
print(r.status_code)
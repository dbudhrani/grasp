import requests

def _get(*args, **kwargs):
  url = kwargs.get('url') 
  assert url
  if not (url.startswith('http://') or url.startswith('https://')):
    url = 'http://' + url
  response = requests.get(url)
  content = response.content
  print(content)
  return content


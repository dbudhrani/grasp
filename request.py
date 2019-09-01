import requests

def _get(*args, **kwargs):
  url = kwargs.get('url') 
  assert url
  response = requests.get(url)
  content = response.content
  print(content)
  return content


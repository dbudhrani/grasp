import requests

def _get(url):
  response = requests.get(url)
  content = response.content
  print(content)
  return content


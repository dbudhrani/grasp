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

def _post(*args, **kwargs):
  raise NotImplementedError

def _put(*args, **kwargs):
  raise NotImplementedError

def _delete(*args, **kwargs):
  raise NotImplementedError

def route(*args, **kwargs):
  method = kwargs.get('method')

  if method == 'GET': return _get(*args, **kwargs)
  if method == 'POST': return _post(*args, **kwargs)
  if method == 'PUT': return _put(*args, **kwargs)
  if method == 'DELETE': return _delete(*args, **kwargs)

  raise Exception('Invalid method: {}'.format(method))

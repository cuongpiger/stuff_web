import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"



get_response = requests.get(endpoint) # API - application programming interface
print(get_response.text)
"""
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.27.1", 
    "X-Amzn-Trace-Id": "Root=1-627a6af7-715c052927f5e7af604f24c7"
  }, 
  "json": null, 
  "method": "GET", 
  "origin": "222.254.174.19", 
  "url": "https://httpbin.org/anything"
}
"""

# HTTP request -> HTML
# REST API HTTP request -> JSON
# JavaScript Object Notation ~ Python Dict
print(get_response.json())
"""
{'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.27.1', 'X-Amzn-Trace-Id': 'Root=1-627a6af7-715c052927f5e7af604f24c7'}, 'json': None, 'method': 'GET', 'origin': '222.254.174.19', 'url': 'https://httpbin.org/anything'}
"""
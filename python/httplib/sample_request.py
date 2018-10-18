import logging
logging.basicConfig(level='DEBUG')

from ddtrace import patch
patch(httplib=True)

import httplib
from ddtrace import config, Pin
config.http.trace_headers('*', integrations='httplib')

url = 'example.com'
path = '/'
headers = {'user-agent': 'my-app/0.0.1'}

conn = httplib.HTTPConnection(url)
conn.request("GET", path, None, headers)

response = conn.getresponse()

print ('Response headers...')
print (response.getheaders())
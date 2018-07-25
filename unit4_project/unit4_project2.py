import wsgiref.simple_server
import urllib.parse
from lesson06.database import Simpledb


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])

    db = Simpledb('db.txt')

    if path == '/insert':
        ### YOUR CODE HERE ###
    elif path == '/select':
        s = db.select_one(params['key'][0])
        start_response('200 OK', headers)
        if s:
            return [s.encode()]
        else:
            return ['NULL'.encode()]
    elif path == '/delete':
        ### YOUR CODE HERE ###
    elif path == '/update':
        ### YOUR CODE HERE ###
    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]
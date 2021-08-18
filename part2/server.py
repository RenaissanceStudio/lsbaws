from wsgiref.simple_server import make_server
from hello import application

port = 8081

# use built-in WSGI server
httpd = make_server('localhost', port, application)
print('Http Server started on port %d' % port)

httpd.serve_forever()
from wsgiref.simple_server import make_server

def aplicacion(env, start_response):
  headers = [('Content-Type','text/plain')] 
  
  start_response('200 ok', headers)
  
  # return 'Hola desde el servidor en tu pc'.encode('utf-8')
  return ['Hola desde el servidor en tu pc'.encode('utf-8')]

server = make_server('localhost',8000,aplicacion)
server.serve_forever()
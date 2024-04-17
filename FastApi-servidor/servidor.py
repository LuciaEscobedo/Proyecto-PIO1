from wsgiref.simple_server import make_server

# Define una función que maneje las solicitudes web
def application(env, start_response):
    # Establece el código de estado y las cabeceras de la respuesta HTTP
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]

    # Llama a la función 'start_response' para enviar la respuesta HTTP al cliente
    start_response(status, headers)

    # El cuerpo de la respuesta HTTP que será enviada al cliente
    response_body = b"<h1>Holis!</h1><p> Soy Lucia! </p>"

    # Devuelve el cuerpo de la respuesta HTTP
    return [response_body]

# Crea un servidor web en el puerto 8000
with make_server('', 8000, application) as server:
    print("Serving on port 8000...")
    # Inicia el servidor y entra en un bucle para manejar las solicitudes entrantes
    server.serve_forever()


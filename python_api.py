from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para el método GET
@app.route('/', methods=['GET'])
def get_hello():
    return 'Hola'

# Ruta para el método POST
@app.route('/', methods=['POST'])
def post_body():
    # Verificar si el cuerpo de la solicitud está presente
    if request.json:
        # Obtener el cuerpo de la solicitud
        body = request.json
        # Devolver el mismo cuerpo como respuesta
        return jsonify(body)
    else:
        return 'Error: El cuerpo de la solicitud es necesario para el método POST', 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

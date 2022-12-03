#importar modulod de flask y jsonify
from flask import Flask, jsonify

#inicializar servidor de flask
app = Flask(__name__)

#testiar el servidor
@app.route('/ping')
def ping():
    return jsonify({'respond':'pong!'})

#endpoint para usuarios
@app.route('/users/<city_id>')
def users(city_id):
    user_list = [
        [0,1,2,3],
        [4,5,6,7],
        [8,9,10,11]
    ]
    return jsonify({'users':user_list[int(city_id)]})

#endpoint para movimientos de usuarios
@app.route('/movements/<user_id>')
def movements(user_id):
    mov_list = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [5,6,7,8],
        [9,10,11,12],
        [1,2,3,4],
        [1,2,3,4],
        [9,10,11,12],
        [9,10,11,12],
        [5,6,7,8],
        [5,6,7,8],
        [5,6,7,8],
    ]
    return jsonify({'movements':mov_list[int(user_id)]})

#invacamos el servidor cuando se ejecute el programa
if __name__ == '__main__':
    app.run(debug=True,port=5000)
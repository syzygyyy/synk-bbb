# vulnerable_code.py
import os
import pickle
import base64
from flask import Flask, request, jsonify
from Crypto.Cipher import DES

app = Flask(__name__)

SECRET_KEY = 'mysecretkey'

@app.route('/unsafe_deserialization', methods=['POST'])
def unsafe_deserialization():
    serialized_data = request.form.get('data')
    data = base64.b64decode(serialized_data)
    deserialized_data = pickle.loads(data)
    return jsonify(deserialized_data)

@app.route('/weak_encryption', methods=['POST'])
def weak_encryption():
    message = request.form.get('message')
    des = DES.new(SECRET_KEY, DES.MODE_ECB)
    encrypted_message = des.encrypt(message)
    return base64.b64encode(encrypted_message).decode('utf-8')

@app.route('/command_injection', methods=['POST'])
def command_injection():
    filename = request.form.get('filename')
    os.system(f'cat {filename}')
    return 'File content displayed'

if __name__ == '__main__':
    app.run()

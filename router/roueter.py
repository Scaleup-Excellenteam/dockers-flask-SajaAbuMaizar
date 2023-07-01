from flask import Flask, request, jsonify
import os
import subprocess
import tempfile

app = Flask(__name__)


@app.route('/code', methods=['POST'])
def receive_code():
    code = request.files['file']
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        code.save(temp_file.name)
        code_path = temp_file.name
    return jsonify({'message': 'Code received successfully', 'code_path': code_path})


@app.route('/execute', methods=['GET'])
def execute_code():
    language = request.args.get('language')
    code_path = request.args.get('code_path')
    if language == 'java':
        result = subprocess.run(['java', '-jar', '/dockers-flask-SajaAbuMaizar/java-executor/executor.jar', code_path],
                                capture_output=True)
        output = result.stdout.decode()
        error = result.stderr.decode()
    elif language == 'python':
        result = subprocess.run(['python', '/dockers-flask-SajaAbuMaizar/python-executor/executor.py', code_path],
                                capture_output=True)
        output = result.stdout.decode()
        error = result.stderr.decode()
    elif language == 'dart':
        result = subprocess.run(['/dockers-flask-SajaAbuMaizar/dart-executor/executor', code_path], capture_output=True)
        output = result.stdout.decode()
        error = result.stderr.decode()
    else:
        return jsonify({'error': 'Invalid language'})

    return jsonify({'output': output, 'error': error})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

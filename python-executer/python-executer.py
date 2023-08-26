from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)


@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.files['file']
    code.save('main.py')
    result = subprocess.run(['python', 'main.py'], capture_output=True)
    output = result.stdout.decode()
    error = result.stderr.decode()
    return jsonify({'output': output, 'error': error})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

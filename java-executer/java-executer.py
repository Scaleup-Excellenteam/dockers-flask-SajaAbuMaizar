from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)


@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.files['file']
    code.save('main.java')
    result = subprocess.run(['javac', 'main.java'], capture_output=True)
    if result.returncode != 0:
        error = result.stderr.decode()
        return jsonify({'error': error})

    result = subprocess.run(['java', '-cp', 'main'], capture_output=True)
    output = result.stdout.decode()
    error = result.stderr.decode()
    return jsonify({'output': output, 'error': error})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

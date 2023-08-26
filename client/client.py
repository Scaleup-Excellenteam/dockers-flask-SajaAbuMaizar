from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/execute', methods=['POST'])
def execute_code():
    code_file = request.files['code']
    language = request.form['language']

    files = {'file': code_file}
    response = requests.post(f'http://router:5000/code', files=files)
    if response.status_code != 200:
        return 'Failed to send code file'

    response = requests.get(f'http://router:5000/execute?language={language}')
    if response.status_code != 200:
        return 'Failed to execute code'

    data = response.json()
    output = data.get('output')
    error = data.get('error')

    return render_template('result.html', output=output, error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

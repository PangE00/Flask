from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/message')
def get_message():
    return jsonify({'message': '연결 성공했어 축하해!'})


if __name__ == '__main__':
    app.run(debug=True)
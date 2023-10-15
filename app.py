from flask import Flask, render_template, jsonify
from flask_cors import CORS
from pymongo import MongoClient

client = MongoClient('mongodb+srv://gghttp3195:3195@pang.kukxz34.mongodb.net/pang?retryWrites=true&w=majority')

db = client.pang
collection = db.urls

cursor = collection.find({}, {"_id": 0, "url": 1})
urls = [document["url"] for document in cursor]  # Extracting all URLs from the cursor

client.close()

app = Flask(__name__, template_folder='templates')
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/message')
def get_message():
    return jsonify({'message': urls})


if __name__ == '__main__':
    app.run(debug=True)

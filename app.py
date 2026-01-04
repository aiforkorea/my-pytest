# app.py
from flask import Flask, jsonify

app = Flask(__name__)

# 첫 화면 (홈페이지)
@app.route('/')
def home():
    return "Hello, World!"

# 데이터를 주는 주소 (API)
@app.route('/info')
def get_info():
    return jsonify({"name": "Gemini", "status": "Happy"})

if __name__ == '__main__':
    app.run(debug=True)
"""
conda install flask
pip install flask-cors
pip install pywinauto
"""
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/api/speech')
def stt():
    args_dict = request.args.to_dict()
    nickname = args_dict["nickname"]
    text = args_dict["text"]
    print(f'{nickname} : {text}')

    return jsonify({ 'data': args_dict, 'response': '데이터 전달 완료' })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3334)

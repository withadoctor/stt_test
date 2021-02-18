"""
conda create -n stt python=3.6 -y
activate stt
conda install flask
pip install flask-cors
pip install pywinauto
pip install pyinstaller
pyinstaller --add-data "templates;templates" --add-data "static;static" server.py
"""
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/api/speech')
def stt():
    args_dict = request.args.to_dict()
    nickname = args_dict["nickname"]
    text = args_dict["text"]
    print(f'{nickname} : {text}')

    return jsonify({ 'data': args_dict, 'response': '데이터 전달 완료' })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3334)

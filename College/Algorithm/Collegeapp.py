# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, send_file
from QACollege import get_answer, load_user_data, load_all_data
from flask_cors import CORS
from werkzeug.utils import secure_filename
from urllib.parse import unquote
# 在启动服务器之前，加载所有数据
load_all_data()

app = Flask(__name__)
CORS(app)


@app.route('/api/get_answer', methods=['POST'])
def api_get_answer():
    data = request.get_json(force=True)
    question = data.get('message', '')
    reset = data.get('reset', False)
    scene = data.get('scenename', '')
    if question:
        answer = get_answer(question, scene, reset=reset)
        return jsonify(answer)
    else:
        return jsonify({'message': 'No question provided.'}), 400


@app.route('/get_file/<scenename>/<filename>')
def get_file(scenename, filename):
    file_path = f"../Data/电机/{scenename}/{filename}"  # 根据场景名称和文件名构建文件路径
    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(host='101.132.161.92', port=5020, debug=True)

from flask import Blueprint, request, jsonify, session, redirect
import sqlite3
import os
from PIL import Image

bp_api = Blueprint('api_bp', __name__)
DB = 'dbzinho.db'
PASTA_ARQ = 'arquivos'
os.makedirs(PASTA_ARQ, exist_ok=True)

@bp_api.route('/up', methods=['POST'])
def up():
    a = request.files['arq']
    if not a.filename or not a.filename.endswith(('.png', '.jpg')):
        return jsonify({'erro': 'arquivo invalido'}), 400
    path = os.path.join(PASTA_ARQ, a.filename)
    a.save(path)
    try:
        img = Image.open(path)
        img.verify()
        return jsonify({'ok': 'upload ok'}), 200
    except:
        os.remove(path)
        return jsonify({'erro': 'processo falhou'}), 400

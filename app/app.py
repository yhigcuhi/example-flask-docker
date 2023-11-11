"""
flask run エントリーポイント
"""
# flaskベース
from flask import Flask, render_template, request, jsonify
# CORS用
from flask_cors import CORS
# ログ設定用
import logging
# API-keyのヘッダーの独自アノテーション
from auth.auth_key import api_key
# 環境設定ファイル読み込み用
from dotenv import load_dotenv
import os, subprocess
# 画像→base64用
import base64

# .envファイル読み込み
load_dotenv()
""" Flaskのサーバー起動コンストラクタ """
# TODO:なんかキモいので __init__.py(外だし)にしたい...やり方 よく分からん
app = Flask(__name__)
# CORS 設定
ACCESS_ALLOW_ORIGINS = os.environ['ACCESS_ALLOW_ORIGINS']
cors = CORS(app, resources={r'/api/*': { 'origins': ACCESS_ALLOW_ORIGINS.split(',') }})
# ログファイル出力
app.logger.setLevel(logging.DEBUG)
log_handler = logging.FileHandler('logs/DEBUG.log')
log_handler.setLevel(logging.DEBUG)
app.logger.addHandler(log_handler)
# SSHホスト
SSH_HOST = os.environ['SSH_HOST']
KICK_COMMAND = os.environ['KICK_COMMAND']

""" ルーティング定義 """
# TODO:上の外だしで ルーティング定義もやりたい まぁ特にないから別にいいが
"""
開発 ヘルスチェック用
"""
@app.route('/')
def index():
    # templates/xxx.htmlの画面表示しろ、bind 変数渡して (テンプレート側のhtml変えてもリロードされないの注意...なんかないの)
    return render_template('index.html')

"""
ファイルアップロード お試し
"""
@app.route('/api/v1/upload', methods=['POST'])
@api_key
def upload():
    # multipart/form-data リクエスト → ファイル取得
    file = request.files['image'] # name="image" の画像ファイル取得
    # 画像ファイル読み込み → base64文字列
    base64_image_str = base64.b64encode(file.read()).decode('utf-8')
    # スクリプト実行
    proc = subprocess.run([f'ssh {SSH_HOST} ' f'{KICK_COMMAND}', '-m'], shell=True)
    app.logger.debug(proc.returncode)
    # TODO:ファイルローカルセーブ → s3アップロードかな...
    return jsonify({
        'data': {
            # base64 (UTF-8でデコード)された文字列をレスポンスボディとして返却 → 画面側で画面表示
            'upload_image': base64_image_str
        }
    })
    # 初期で試した時
    # return f'{file.filename}が{base64ImageStr}アップロードされました'

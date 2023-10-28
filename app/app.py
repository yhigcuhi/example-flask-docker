"""
flask run エントリーポイント
"""
from flask import Flask, render_template, request
import logging
import os

""" Flaskのサーバー起動コンストラクタ """
# TODO:なんかキモいので __init__.py(外だし)にしたい...やり方 よく分からん
app = Flask(__name__)
# ログファイル出力
app.logger.setLevel(logging.DEBUG)
log_handler = logging.FileHandler('logs/DEBUG.log')
log_handler.setLevel(logging.DEBUG)
app.logger.addHandler(log_handler)

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
def upload():
    # TODO: 次...CORSないからaxiosエラーになるっぽいので解決
    # multipart/form-data リクエスト → ファイル取得
    file = request.files['image'] # name="image" の画像ファイル取得
    # TODO:ファイルローカルセーブ → s3アップロードかな...
    # file.save(os.path.join('./static/image', file.filename))
    return f'{file.filename}がアップロードされました'

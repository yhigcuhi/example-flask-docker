from flask import Flask, render_template

""" Flaskのサーバー起動コンストラクタ """
app = Flask(__name__)

"""
 エントリーポイント
"""
@app.route('/')
def index():
    # templates/xxx.htmlの画面表示しろ、bind 変数渡して (テンプレート側のhtml変えてもリロードされないの注意...なんかないの)
    return render_template('index.html')


from flask import request, make_response, jsonify
from dotenv import load_dotenv
import os

# .envファイル読み込み
load_dotenv()
# API keyを環境変数から
API_KEY = os.environ['API_KEY']

# デコレーター用の関数
# 引数に、デコレータ対象の関数を受け取る
"""
API key認証
"""
def api_key(func):
    """デコレータ関数にて、API-keyの妥当性と必須のチェックを行う"""
    def decorator(*args, **kwargs):
        # デコレータ付与先の関数のリクエストから判定 値の妥当性
        if not request.headers.get('X-API-KEY') == API_KEY:
            return make_response(jsonify({'error': 'is not api key'}), 400)

        # 実行する(正常)
        return func(*args, **kwargs)
    return decorator

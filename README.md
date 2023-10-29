# example-flask-docker
Python Flask + Docker 環境のお試し

## ゴール
localhost:3000 (react viteで作成したページ) アップロード → localhost:5001/api/v1/upload → localhost:3000 反応 → localhost:3000/complete 画面 

## setup
1. .env.exampleの内容を参考に .env用意 (面倒なら cp .env.example .env でオケ)
1. docker compose build
1. docker compose up -d
1. docker compose run --rm front yarn install
1. docker compose down
1. docker compose up -d
1. localhost:5001、localhost:3000(.envの内容によりけり)で画面出たら完了

※ flask 側はよく分からんが docker compose exec flask ashで入れる

## 参考
- [Docker Flask 構築](https://zenn.dev/tatausuru/articles/35e123034b98ba)
- [Flask LaravelのMVCぽくしたの参考](https://michi-programming.hatenablog.com/entry/2022/11/07/200000)
- [Flask CORS導入の参考](https://memorandom.whitepenguins.com/posts/flask-cors/)
- [PyCharm pythonインタプリタ(ライブラリ読み込みとかの設定)](https://pleiades.io/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote)
- [Python デコレーター関数](https://www.yoheim.net/blog.php?q=20160607)
- [Flask requestを利用したデコレーター関数](https://qiita.com/5zm/items/c3f004291a87cdbce0b9)
- [Python .env環境設定ファイル読み込み](https://zenn.dev/nakashi94/articles/9c93b6a58acdb4)

## pip install 結果を requirements.txtに記載 ... 自動更新ではない
ライブラリ追加後...
pip freeze で 現在の一覧を見て、追加されたライブラリを requirements.txtに追加

## 初回構築時の作業内容(setupじゃないのですまん メモ)
### flask
1. .env.example, .env用意
1. requirements.txtを /app/requirements.txtにようい 内容 pip でインストールする Flaskの最新バージョン
1. app.py(Flask 起動するエントリーポイントのpython)を /app/app.py (内容下記)
1. docker 整備し docker compose up -d
1. cd app
1. curl https://www.toptal.com/developers/gitignore/api/vim,linux,macos,flask,windows,composer,intellij,sublimetext,visualstudio,visualstudiocode >> .gitignore
1. cd ../

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'
```

### front(react + vite)
1. .env.example, .env用意
1. docker compose up -d
1. docker compose run --rm front yarn create vite
1. > project name: ./
1. > select framework: React
1. > select variant: Javascript
1. cd front
1. curl https://www.toptal.com/developers/gitignore/api/vim,linux,macos,react,node,windows,intellij,sublimetext,visualstudio,visualstudiocode >> .gitignore
1. cd ../
1. docker compose run --rm front yarn install && yarn build
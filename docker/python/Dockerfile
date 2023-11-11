# python3での構築
FROM python:3.9-alpine

# OSインストール
RUN apk update && \
    apk add  \
    openssh-client

# 作業ディレクトリ
WORKDIR /usr/src/app
# 作業ディレクトリに依存パッケージ一覧配置
COPY ../../app/requirements.txt ./

# pip ... pythonパッケージ管理ファイル
RUN pip install --upgrade pip
# requirements.txt ... 依存パッケージ一覧ファイルs
RUN pip install -r requirements.txt
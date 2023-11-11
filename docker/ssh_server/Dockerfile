# ubuntuで SSHサーバー先組む
FROM ubuntu:18.04

# sshサーバをインストールします
RUN apt-get update \
    && apt-get install -y \
    openssh-server \
    openssh-client

# これが無いとsshdが起動しないっぽい
RUN mkdir /var/run/sshd
# rootのパスワードをpasswdに設定します。ただし、公開鍵認証でのアクセスなので使用しませんが。。
RUN echo 'root:password' | chpasswd
# sshのrootでのアクセスを許可します
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# sshのポートを22 => 20022に変更します
RUN sed -i 's/#Port 22/Port 20022/' /etc/ssh/sshd_config
# ホスト側にある公開鍵をイメージ側に登録します
COPY ../../ssh/docker_ssh_id_rsa.pub /root/.ssh/authorized_keys

# SSHポート解放
EXPOSE 20022
CMD ["/usr/sbin/sshd", "-D"]

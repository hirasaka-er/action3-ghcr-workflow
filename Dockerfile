from python:3.8
#ワークディレクトリを作成
workdir /var/www

#ホスト側のhello.pyをコンテナ側の[var/www]へコピー
copy ./src /var/www

run pip install flask

CMD python hello.py

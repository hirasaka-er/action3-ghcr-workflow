# 参考サイトのソースをそのまま貼り付け
# https://qiita.com/std-flower/items/de9590b00c3efc928dc4

from flask import Flask

#Flaskオブジェクトを生成、[__name__]はおまじない的なやつ
app = Flask(__name__)

#ブラウザで[localhost]の仮想ディレクトリルートが指定された場合の挙動（hello worldを出力）
@app.route('/')
def hello():
    return 'hello world 2'

#webサーバを起動
if __name__ == '__main__':
    app.run(debug='true',host='0.0.0.0',port='8888')

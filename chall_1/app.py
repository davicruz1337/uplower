from flask import Flask
from api import bp_api
from frontend import bp_front

app = Flask(__name__)
app.secret_key = 'gankd'
app.config['UPLO'] = 'arquivos'

app.register_blueprint(bp_api)
app.register_blueprint(bp_front)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

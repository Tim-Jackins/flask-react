from flask import Flask, render_template, send_from_directory
import os
from decouple import config


class Config(object):
    SECRET_KEY = config('SECRET_KEY') or 'sssh-its-a-secret'
    DEBUG = config('DEBUG') or 'True'


app = Flask(__name__, static_folder='my-app/build')
app.config.from_object(Config)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != '' and os.path.exists('my-app/build/' + path):
        return send_from_directory('my-app/build', path)
    else:
        return send_from_directory('my-app/build', 'index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

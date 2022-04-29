from flask import Flask

from main.views import main_blueprint
from loader.views import loader_blueprint

app = Flask(__name__)

# Ограничиваем максимальный размер файла 8-ю мегабайтами.
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

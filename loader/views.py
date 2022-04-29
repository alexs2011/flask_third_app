from flask import Blueprint, abort, render_template, request, send_from_directory

from logger import logger
from utility.utils import save_new_post, validate_data

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder='templates')


@loader_blueprint.route("/post", methods=["GET"])
def page_post_form():
    """
    Страница с формой создания нового поста.
    """
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    """
    Проверяет корректность и сохраняет полученные через post-запрос данные поста.
    """
    try:
        validate_data(request)
    except ValueError as e:
        logger.exception(e)
        return str(e)
    except TypeError as e:
        logger.exception(e)
        return str(e)
    try:
        new_post = save_new_post(request)
    except Exception as e:
        logger.exception(e)
        abort(500)
    return render_template("post_uploaded.html", post=new_post)


@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    """
    Позволяет получить доступ к данным в директории загрузки.
    """
    return send_from_directory("uploads", path)

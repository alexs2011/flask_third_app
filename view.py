from flask import render_template

from app import app
from logger import logger


@app.errorhandler(404)
def page_not_found(e):
    """
    Страница для ошибки 404 Page Not Found.
    """
    logger.info(e)
    return render_template("404.html"), 404

from flask import request, render_template, send_from_directory

from app import app


@app.route("/")
def page_index():
    return render_template("index.html")


@app.route("/list")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

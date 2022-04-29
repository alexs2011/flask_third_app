from flask import Blueprint, abort, render_template, request

from utility.utils import find_posts_by_phrase, load_posts, validate_JSON

main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')


@main_blueprint.route('/')
def page_index():
    """
    Начальная страница с формой поиска и добавления постов.
    """
    return render_template("index.html")


# @main_blueprint.route("/list")
# def page_all_posts():
#     """
#     Страница со всеми загруженными постами.
#     """
#     try:
#         posts = load_posts()
#         validate_JSON(posts)
#     except:
#         abort(500)
#     return render_template('post_list.html', posts=posts)

@main_blueprint.route('/list')
@main_blueprint.route('/search')
def search_page():
    """
    Страница с результатами поиска по тексту постов.
    """
    try:
        posts = load_posts()
        validate_JSON(posts)
    except:
        abort(500)
    phrase = request.args.get('s')
    if phrase:  # если в запросе есть параметр s, т.е. перешли по роуту '/search'
        filtered_posts = find_posts_by_phrase(posts, phrase)
        return render_template('post_list.html', posts=filtered_posts, phrase=phrase)
    # иначе перешли по '/list'
    return render_template('post_list.html', posts=posts)

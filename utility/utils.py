import json
from datetime import datetime

import flask

from config import POST_PATH, UPLOAD_FOLDER


def load_posts() -> list[dict]:
    """
    Загружает данные из файла формата JSON.
    """
    with open(POST_PATH, 'r', encoding='utf-8') as f_in:
        return json.load(f_in)


def save_posts_to_file(posts: list[dict]) -> None:
    """
    Сохраняет данные постов в файл JSON.
    """
    with open(POST_PATH, "w", encoding='utf-8') as f_out:
        json.dump(posts, f_out, ensure_ascii=False, indent=2)


def find_posts_by_phrase(posts: list[dict], phrase: str) -> list[dict]:
    """
    Поиск всех постов, в тексте которых есть phrase.
    """
    filtered_posts = []
    for post in posts:
        if phrase.lower() in post['content'].lower():
            filtered_posts.append(post)
    return filtered_posts


def validate_JSON(posts: list[dict]) -> None:
    """
    Проверка того, считали ли мы из файла список постов.
    """
    if not isinstance(posts, list):
        raise ValueError("Загруженные данные не являются списком.")


def validate_data(request: flask.Request) -> None:
    """
    Проверка того, выбрал ли пользователь изображение для загрузки и написал ли он текст поста, а также того,
    является ли загруженный файл изображением.
    """
    img = request.files['picture']
    text = request.form['content']
    if not img or not text:
        raise ValueError("Ошибка загрузки")
    if img.content_type not in ["image/jpeg", "image/png"]:
        raise TypeError("Загруженный файл - не картинка")


def save_new_post(request: flask.Request) -> dict:
    """
    Добавляет загруженный пост в список постов и сохраняет этот список в файл формата JSON.
    """
    img = request.files['picture']
    content = request.form['content']
    posts = load_posts()
    filename = save_img_to_file(img)
    new_post = {
        "pic": filename,
        "content": content
    }
    posts.append(new_post)
    save_posts_to_file(posts)
    return new_post


def save_img_to_file(img) -> str:
    """
    Добавляет к имени загруженного изображения дату и время загрузки, и сохраняет его на диск.
    """
    time = datetime.now()
    filename = f"{time.strftime('%Y_%m_%d_%H_%M_%S')}_{img.filename}"
    img.save(f"{UPLOAD_FOLDER}/{filename}")
    return filename

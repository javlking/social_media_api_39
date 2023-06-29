from flask import Blueprint, request
from database.postservice import get_all_posts_db, get_exact_post_db, delete_exact_post_db, change_post_text_db, \
    add_new_post_db, post_new_photo_db, create_post_for_hashtag


post_bp = Blueprint('user_post', __name__, url_prefix='/post')


# Получить все посты
@post_bp.route('/', methods=['GET'])
def get_all_user_posts():
    all_posts = get_all_posts_db()
    if all_posts:
        return {'status': 1, 'message': all_posts}
    return {'status': 0, 'message': 'Not found'}


# Получить определенный пост
@post_bp.route('/<int:post_id>', methods=['GET'])
def get_exact_post(post_id: int):
    exact_post = get_exact_post_db(post_id)
    if exact_post:
        return {'status': 1, 'message': exact_post}
    return {'status': 0, 'message': 'Not found'}


# Опубликовать пост
@post_bp.route('/upload_post', methods=['POST'])
def create_post(post_text: str, user_id: int):
    # получаем из фронт части фотографию
    file = request.files.get('post_photo', '')
    file.save(f'user_images/{file.filename}')

    # получить хештеги из фронт части
    hashtags = request.json.get('hashtags')

    # сохраняем в базу и получаем id для фото
    new_photo_id = post_new_photo_db(user_id, file.filename)

    # сохраняем сам пост
    new_post_id = add_new_post_db(user_id=user_id, photo_id=new_photo_id, post_text=post_text)

    # Если из фронт части пришли хештеги
    if hashtags:
        create_post_for_hashtag(new_post_id, hashtags)

    return {'status': 1, 'message': 'пост добавлен'}


# Изменить определенный пост
@post_bp.route('/<int:post_id>', methods=['PUT'])
def change_user_post(post_id: int):
    new_post_text = request.json.get('new_post_text')

    change_post_text_db(post_id, new_post_text)

    return {'status': 1, 'message': 'пост успешно изменен'}


# Удалить определенный пост
@post_bp.route('/<int:user_id>/<int:post_id>', methods=['DELETE'])
def delete_user_post(user_id: int, post_id: int):
    delete_user_post = delete_exact_post_db(user_id, post_id)
    if delete_user_post:
        return {'status': 1, 'message': 'Post deleted'}
    return {'status': 0, 'message': 'Not found'}

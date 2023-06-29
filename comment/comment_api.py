from flask import Blueprint
from database.postservice import add_comment_post_db, get_exact_post_comments_db, change_user_comment_db, \
    delete_comment_db

comment_bp = Blueprint('comment', __name__, url_prefix='/comment')


# Получить комментарии определенного поста
@comment_bp.route('/<int:post_id>', methods=['GET'])
def get_exact_post_comments(post_id: int):
    exact_post_comments = get_exact_post_comments_db(post_id)
    if exact_post_comments:
        return {'status': 1, 'message': exact_post_comments}
    return {'status': 0, 'message': 'Not found'}


# Публикация комментария
@comment_bp.route('/<int:post_id>/<int:comment_user_id>', methods=['POST'])
def publish_comment(post_id: int, comment_user_id: int, comment_text: str):
    publish_comment = add_comment_post_db(post_id, comment_user_id, comment_text)
    if publish_comment:
        return {'status': 1, 'message': 'Added'}
    return {'status': 0, 'message': 'Not found'}


# Изменить комментарий
@comment_bp.route('/<int:comment_user_id>/<int:comment_id>', methods=['PUT'])
def change_comment(comment_user_id: int, comment_id: int, comment_text: str):
    change_comment = change_user_comment_db(comment_user_id, comment_id, comment_text)
    if change_comment:
        return {'status': 1, 'message': 'Comment changed'}
    return {'status': 0, 'message': 'Not found'}


# удалить комментарий
@comment_bp.route('/<int:comment_user_id>/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_user_id: int, comment_id: int):
    delete_comment = delete_comment_db(comment_user_id, comment_id)
    if delete_comment:
        return {'status': 1, 'message': 'Comment deleted'}
    return {'status': 0, 'message': 'Not found'}

from flask import Blueprint
from database.postservice import get_hashtags_incount_db, get_exact_hashtag_db

hashtag_bp = Blueprint('hashtag', __name__, url_prefix='/hashtag')


# Получить хэштег по количеству
@hashtag_bp.route('/', methods=['GET'])
def get_hashtags(size: int):
    get_hashtags = get_hashtags_incount_db(size)
    if get_hashtags:
        return {'status': 1, 'message': get_hashtags}
    return {'status': 0, 'message': 'Not found'}


# Получить хэштег по названию
@hashtag_bp.route('/<string:hashtag_name>', methods=['GET'])
def get_exact_hashtag(hashtag_name: str):
    get_exact_hashtag = get_exact_hashtag_db(hashtag_name)
    if get_exact_hashtag:
        return {'status': 1, 'message': get_exact_hashtag}
    return {'status': 0, 'message': 'Not found'}

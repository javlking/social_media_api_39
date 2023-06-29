from flask import Blueprint, request
from database.postservice import get_exact_user_photos_db, get_all_photos_db, get_exact_photo_db, \
    change_exact_user_photo_db, delete_exact_user_photo_db, post_new_photo_db

photo_bp = Blueprint('photo', __name__, url_prefix='/photo')


# Получить все фотографии всех пользователей
@photo_bp.route('/', methods=['GET'])
def get_all_photos():
    all_photos = get_all_photos_db()  # Получаем все фотографии
    return {'status': 1, 'message': all_photos}  # Выдаем результат


# Публикация фотографии
@photo_bp.route('/', methods=['POST'])
def publish_photo(user_id: int):
    # Получить фото из фронт части
    file = request.files.get('image', '')
    file.save('user_images/' + file.filename)

    new_photo = post_new_photo_db(user_id, file.filename)

    return {'status': 1, 'message': 'Фото успешно добавлен'}


# Получить фотографии определенного пользователя по user_id
@photo_bp.route('/<int:user_id>', methods=['GET'])
def get_exact_user_photos(user_id: int):
    exact_user_photos = get_exact_user_photos_db(user_id)  # Получаем фотографии пользователя
    if exact_user_photos:  # Если фотографии есть
        return {'status': 1, 'message': exact_user_photos}
    return {'status': 0, 'message': 'Not found'}  # Если фотографий нет


# Получить определенную фотографию по photo_id
@photo_bp.route('/<int:photo_id>', methods=['GET'])
def get_exact_photo(photo_id: int):
    exact_photo = get_exact_photo_db(photo_id)  # Получаем фото по его ID
    if exact_photo:
        return {'status': 1, 'message': exact_photo}
    return {'status': 0, 'message': 'Not found'}  # Если фотографий нет


# Изменить определенную фотографию пользователя
@photo_bp.route('/<int:user_id>/<int:photo_id>', methods=['PUT'])
def change_exact_user_photo(user_id: int, photo_id: int, photo_path: str):
    exact_user_photo = change_exact_user_photo_db(user_id, photo_id, photo_path)
    if exact_user_photo:
        return {'status': 1, 'message': 'photo changed'}


# Удалить определенную фотографию пользователя
@photo_bp.route('/<int:user_id>/<int:photo_id>', methods=['DELETE'])
def delete_user_photo(user_id: int, photo_id: int):
    delete_user_photo = delete_exact_user_photo_db(user_id, photo_id)
    if delete_user_photo:
        return {'status': 1, 'message': 'photo deleted'}
    return {'status': 0, 'message': 'photo not found'}

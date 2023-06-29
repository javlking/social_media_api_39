from database.models import Post, PostPhoto, PostComment, db, HashTag


# Получить все изображения
def get_all_photos_db():
    photos = PostPhoto.query.all()
    return photos


# Получить все изображения определенного пользователя
def get_exact_user_photos_db(user_id):
    exact_user_photo = PostPhoto.query.filter_by(user_id=user_id).first()
    return exact_user_photo


# Получить определенную фоторгафию по photo_id
def get_exact_photo_db(photo_id):
    exact_photo = PostPhoto.query.filter_by(photo_id=photo_id).first()
    return exact_photo


# Изменить определенную фоторгафию пользователя по user_id и photo_id
def change_exact_user_photo_db(user_id, photo_id, photo_path):
    change_exact_user_photo = PostPhoto.query.filter_by(photo_id=photo_id, user_id=user_id).first()
    if change_exact_user_photo:
        change_exact_user_photo.photo_path = photo_path
        db.session.commit()


# Удаляем определенную фотографию пользователя по user_id и photo_id
def delete_exact_user_photo_db(user_id, photo_id):
    delete_exact_user_photo = PostPhoto.query.filter_by(photo_id=photo_id, user_id=user_id).first()
    if delete_exact_user_photo:
        db.session.delete(delete_exact_user_photo)
        db.session.commit()
        return True
    return False


# Получить все посты
def get_all_posts_db():
    posts = Post.query.all()
    return posts


# Получить определенный пост
def get_exact_post_db(post_id):
    exact_post = Post.query.filter_by(post_id=post_id).first()
    return exact_post


# Удалить определенный пост
def delete_exact_post_db(user_id, post_id):
    delete_post = Post.query.filter_by(user_id=user_id, post_id=post_id).first()
    if delete_post:
        db.session.delete(delete_post)
        db.session.commit()
        return True
    return False


# Изменить текст поста
def change_post_text_db(post_id, new_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post:
        post.post_text = new_text
        db.session.commit()
        return True
    return False


# Добавить новый пост
def add_new_post_db(user_id, photo_id, post_text):
    new_post = Post(user_id=user_id, photo_id=photo_id, post_text=post_text)
    db.session.add(new_post)
    db.session.commit()

    return new_post.post_id


# Добавить комментарий к посту
def add_comment_post_db(post_id, comment_user_id, comment_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post:
        new_comment = PostComment(post_id=post_id, user_id=comment_user_id, comment_text=comment_text)
        db.session.add(new_comment)
        db.session.commit()
        return True
    return False


# Получение хештегов по количеству
def get_hashtags_incount_db(size):
    get_hashtags_incount = HashTag.query.all()
    if len(get_hashtags_incount) >= size:
        return get_hashtags_incount[:size]
    return False


# Получение определенного хештега
def get_exact_hashtag_db(hashtag_name):
    get_exact_hashtag = HashTag.query.filter_by(hashtag_name=hashtag_name).all()
    if get_exact_hashtag:
        return get_exact_hashtag
    return False


# Добавить пост под хештег
def create_post_for_hashtag(post_id, hashtags):
    created_hashtags = []

    for hashtag_name in hashtags:
        new_hashtag_post = HashTag(post_id=post_id, hashtag_name=hashtag_name)
        created_hashtags.append(new_hashtag_post)

    db.session.add_all(created_hashtags)
    db.session.commit()

    return True


# Получить комментарии определенного поста
def get_exact_post_comments_db(post_id):
    exact_post_comments = PostComment.query.filter_by(post_id=post_id).first()
    if exact_post_comments:
        return exact_post_comments
    return False


# Изменение комментария

def change_user_comment_db(comment_user_id, comment_id, comment_text):
    change_user_comment = PostComment.query.filter_by(user_id=comment_user_id, comment_id=comment_id).first()
    if change_user_comment:
        change_user_comment.comment_text = comment_text
        db.session.commit()
        return True
    return False


# Удаление комментария

def delete_comment_db(comment_user_id, comment_id):
    delete_comment = PostComment.query.filter_by(user_id=comment_user_id, comment_id=comment_id).first()
    if delete_comment:
        db.session.delete(delete_comment)
        db.session.commit()
        return True
    return False


# загрузка фотографии
def post_new_photo_db(user_id, photo_path):
    new_post_photo = PostPhoto(user_id=user_id, photo_path=photo_path)

    db.session.add(new_post_photo)
    db.session.commit()

    return new_post_photo.photo_id

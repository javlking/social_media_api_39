from database.models import User, Password, db


# Регистрация
def register_user_db(**user_data):
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()


# Проверка пользователя по почте
def check_user_db(email):
    cheker_email = User.query.filter_by(email=email).first()
    if cheker_email:
        return True
    return False


# Проверка пароля пользователя
def check_user_password_db(email, password):
    cheker_email = User.query.filter_by(email=email).first()
    cheker_pass = Password.query.filter_by(password=password).first()
    if cheker_email and cheker_pass:
        return True
    return False


# Получить всех пользователей из базы
def get_all_users_db():
    users = User.query.all()
    return users


# Получить определенного пользователя
def get_exact_user_db(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    return user


# Удалить пользователя из базы
def delete_user_db(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

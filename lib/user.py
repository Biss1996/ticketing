# from lib.models import session, User

# def create_user(username, email):
#     user = User(username=username, email=email)
#     session.add(user)
#     session.commit()
#     return user

# def get_all_users():
#     return session.query(User).all()

# def get_user_by_id(user_id):
#     return session.query(User).filter_by(id=user_id).first()

# def update_user(user_id, username=None, email=None):
#     user = get_user_by_id(user_id)
#     if user:
#         if username:
#             user.username = username
#         if email:
#             user.email = email
#         session.commit()
#     return user

# def delete_user(user_id):
#     user = get_user_by_id(user_id)
#     if user:
#         session.delete(user)
#         session.commit()
#     return user

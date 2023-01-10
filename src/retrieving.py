from main import Base, Session, User, engine

local_session =  Session(bind=engine)

users = local_session.query(User).all()

for user in users:
    print(user.username)
    print(user.id)

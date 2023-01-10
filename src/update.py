from main import Base, Session, User, engine

local_session =  Session(bind=engine)

user = local_session.query(User).filter(User.username=='muzmail').first()
user.username = 'master'
user.email = 'master@gmail.com'

local_session.commit()

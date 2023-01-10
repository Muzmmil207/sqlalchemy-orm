from main import Session, User, engine

local_session =  Session(bind=engine)
user = local_session.query(User).filter(User.username=='muzmail').first()
local_session.delete(user)
local_session.commit()

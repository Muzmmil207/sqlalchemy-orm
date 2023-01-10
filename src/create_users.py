from main import Session, User, engine

local_session =  Session(bind=engine)
new_user = User(username='muzamil', email='mly88207@gmail.com')
local_session.add(new_user)
local_session.commit()

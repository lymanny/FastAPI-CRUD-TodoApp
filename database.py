from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



######################## Connect with sqlite ########################

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

Base = declarative_base()




######################## Connect with postgresql ########################

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1234@localhost/TodoApplicationDatabase'
#
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
#
# SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)
#
# Base = declarative_base()
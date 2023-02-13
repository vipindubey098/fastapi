from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Fastapi says, create a variable called:
SQLALCHAMY_DATABASE_URL = 'sqlite://blog.db'

# engine = create_engine(SQLALCHAMY_DATABASE_URL, echo =True)

# We will not use echo as true rather than we will use connect_args as per fastapi

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Next we need to declare a Mapping for that we need import declarative_base from sqlalchemy
Base = declarative_base()


# After that we need to create a session 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(config('DB_URL'), pool_pre_ping=True)
Session = sessionmaker(bind=engine)

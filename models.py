from sqlalchemy import Column, Integer, String, DateTime, Text, MetaData
from sqlalchemy.ext.declarative import declarative_base

from database_engine import engine


metadata = MetaData(schema='Restaurant')
Base = declarative_base(bind=engine, metadata=metadata)


class Transaction(Base):
    __tablename__ = 'Transaction'

    id = Column('ID', String(100), primary_key=True)
    store_id = Column('STORE_ID', Integer)
    created_time = Column('CREATED_TIME', DateTime)
    transaction_json = Column('TXN_JSON', Text)

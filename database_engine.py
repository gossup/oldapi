from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_database_engine():
    connection_string = 'ibm_db_sa+pyodbc400://{username}:{password}@{host}:{port}/{database};currentSchema={schema}'.format(
        username='',
        password='',
        host='',
        port='',
        database='',
        schema=''
    )
    return create_engine(connection_string)


engine = create_database_engine()


def create_session():
    Session = sessionmaker(bind=engine)
    return Session()


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = create_session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

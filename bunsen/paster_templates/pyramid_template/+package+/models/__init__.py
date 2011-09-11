import logging
import transaction
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from zope.sqlalchemy import ZopeTransactionExtension

log = logging.getLogger(__name__)

Session = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

def initialize_sql(engine):
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    transaction.commit()

import logging
import transaction
import sqlahelper

log = logging.getLogger(__name__)

Session = sqlahelper.get_session()
Base = sqlahelper.get_base()

def initialize_sql():
    Base.metadata.create_all()
    transaction.commit()

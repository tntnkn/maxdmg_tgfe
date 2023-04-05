from sqlalchemy     import (
    Table, 
    Column, 
    Integer, 
    Boolean,
)
from .Metadata      import metadata_obj


tg_users_table = Table(
    'tg_user',
    metadata_obj,
    Column('tg_id', Integer, primary_key=True, nullable=False),
    Column('is_messagable', Boolean, nullable=False, default=True),
)


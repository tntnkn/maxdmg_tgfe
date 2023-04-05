from sqlalchemy     import (
    Table, 
    Column, 
    Integer, 
    Date,
    Time,
    ForeignKey,
)
from .Metadata      import metadata_obj


download_dates_table = Table(
    'download_date',
    metadata_obj,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date', Date, nullable=False),
    Column('time', Time, nullable=False),
    Column('tg_user_id', Integer, ForeignKey('tg_user.tg_id'), 
           nullable=False)
)


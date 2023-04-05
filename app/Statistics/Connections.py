from sqlalchemy.engine      import URL
from sqlalchemy.ext.asyncio import create_async_engine

from ..bot              import config

url = URL.create(
    drivername='sqlite+aiosqlite',
    host='/stats_db/test.db'
)

a_engine = create_async_engine(
    'sqlite+aiosqlite:///stats_db/test.db'
)


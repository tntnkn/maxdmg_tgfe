from sqlalchemy.engine      import URL
from sqlalchemy.ext.asyncio import create_async_engine

from ..bot                  import config

if config.TEST_DB:
    url = URL.create(
        drivername='sqlite+aiosqlite',
        host='/stats_db/test.db'
    )

    a_engine = create_async_engine(
        'sqlite+aiosqlite:///stats_db/test.db'
    )
else:
    url = URL.create(
        drivername='postgresql+asyncpg',
        host='stats_db',
        port='5432',
        database='tgfe_stats_db',
        username='tgfe_stats_admin',
        password=config.STATS_DB_PASS,
    )

    a_engine = create_async_engine(
        url,
        pool_size=10, 
        max_overflow=5,
        connect_args={'timeout': 2},
    )


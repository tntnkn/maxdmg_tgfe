import asyncio
from .Schema        import metadata_obj as __md
from .Connections   import a_engine as __eng
from .Interface import StatsDB



def init_stats_db():
    loop = asyncio.get_event_loop()
    init_stats_db.LOOP_TASK_REF = loop.create_task(
        __init_stats_db())
    return loop


async def __init_stats_db():
    async with __eng.begin() as conn:
        await conn.run_sync(__md.create_all)


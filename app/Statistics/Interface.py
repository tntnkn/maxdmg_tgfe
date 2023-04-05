import datetime
from sqlalchemy     import (
    insert,
    select,
    delete,
    update,
    bindparam,
)
from sqlalchemy     import exc
from .Connections   import a_engine
from .Schema        import (
    tg_users_table, 
    download_dates_table,
)


class StatsDB():
    def __init__(self):
        self.insert_user = insert(tg_users_table)
        self.delete_user = \
            delete(tg_users_table).\
            where(tg_users_table.c.tg_id == \
                  bindparam('tg_user_id') )
        self.set_user_messagability = \
            update(tg_users_table).\
            where(tg_users_table.c.tg_id == \
                  bindparam('tg_user_id') ). \
            values( is_messagable=bindparam('status') )
        self.insert_new_document = insert(download_dates_table)
             
    async def NewUser(self, tg_user_id):
        async with a_engine.connect() as conn:
            try:
                res = await conn.execute(
                    self.insert_user,
                    {'tg_id' : tg_user_id}
                )
            except exc.IntegrityError:
                await self.__ExecUserMessagibility(
                    tg_user_id, True, conn)
            await conn.commit()

    async def SetUserNotMessagable(self, tg_user_id):
        async with a_engine.connect() as conn:
            await self.__ExecUserMessagibility(
                tg_user_id, False, conn)
            await conn.commit()

    async def SetUserMessagable(self, tg_user_id):
        async with a_engine.connect() as conn:
            await self.__ExecUserMessagibility(
                tg_user_id, True, conn)
            await conn.commit()

    async def NewDocumentGenerated(self, tg_user_id):
        async with a_engine.connect() as conn:
            t = datetime.datetime.today() 
            res = await conn.execute(
                self.insert_new_document,
                {'date':t.date(), 
                 'time':t.time(),
                 'tg_user_id':tg_user_id},
            )
            await conn.commit()

    async def __ExecUserMessagibility(
        self, tg_user_id, status, conn):
            res = await conn.execute(
                self.set_user_messagability,
                {'tg_user_id': tg_user_id, 'status': status},
            )



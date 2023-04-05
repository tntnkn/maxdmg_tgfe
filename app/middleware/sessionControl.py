from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler     import CancelHandler
from aiogram import types

from ..Utils                        import (
    SessionLock, 
    update_user_last_action_time
)
from ..Storage                      import Storage
from ..Statistics                   import StatsDB 


class sessionControl(BaseMiddleware):
    async def on_process_update(
            self, 
            update: types.Update, 
            data: dict):
        tg_user_id = sessionControl.__get_tg_id(update)
        if not tg_user_id:
            raise CancelHandler()

        s_h = Storage()
        if not s_h.HasUser(tg_user_id):
            s_h.AddUser(tg_user_id)
            await StatsDB().NewUser(tg_user_id)
        
        if not SessionLock.Lock(tg_user_id):
            raise CancelHandler()

        update_user_last_action_time(tg_user_id)

    async def on_post_process_update(
            self, 
            update: types.Update,
            data_from_handler: list,
            data: dict):
        tg_user_id = sessionControl.__get_tg_id(update)
        if not tg_user_id:
            raise CancelHandler()

        try:
            SessionLock.Unlock(tg_user_id)
        except:
            pass
        
    def __get_tg_id(update):
        tg_user_id = None
        if   "message" in update:
            tg_user_id = update['message']['from']['id']
        elif "callback_query" in update:
            tg_user_id = update['callback_query']['from']['id']
        return tg_user_id


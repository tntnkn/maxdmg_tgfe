import asyncio
from time           import time

from ..Storage      import UsersLoop


class DanglingSessionsManager():
    DANGLING_SESSIONS_CHECKUP_STRIDE   = 20 * 60
    MAX_ALLOWED_DANGLING_TIME          = 20 * 60 
    
    LOOP_TASK_REF = None

    @staticmethod
    def Start():
        loop = asyncio.get_event_loop()
        DanglingSessionsManager.LOOP_TASK_REF = loop.create_task(
            DanglingSessionsManager.dangling_sessions_control_loop())
        return loop

    @staticmethod
    async def dangling_sessions_control_loop():
        while True:
            await asyncio.sleep(
                DanglingSessionsManager.DANGLING_SESSIONS_CHECKUP_STRIDE)
            await DanglingSessionsManager().delete_dangling_sessions()

    @staticmethod
    async def delete_dangling_sessions():
        now = time()
        for s_view in UsersLoop():
            then = s_view.Read('last_action_time')
            if now - then > \
               DanglingSessionsManager.MAX_ALLOWED_DANGLING_TIME:
                s_view.Destroy()


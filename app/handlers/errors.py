from ..Factories    import (
    BackAPIFactory, 
    FormFactory, 
    DocumentFactory,
)
from ..Storage      import (
    UserStorageView, 
    Storage,
)
from ..Utils        import (
    CallbackTransformer, 
    AllowedInputTypeHelper, 
    Send, 
    MessagesArchive, 
    MessageManager
)
from ..Static       import (
    AllowedInputType,
)
from ..Exceptions   import (
    TGFE_BadUserInSystem,
)
from ..validators   import check_input_length
from ..bot          import dp, types
from aiogram.dispatcher.handler     import CancelHandler


back_api = BackAPIFactory.Make()


@dp.errors_handler(exception=TGFE_BadUserInSystem) 
async def message_not_modified_handler(update, exc): 
    back.api.DeleteUser(exc.tg_user_id)
    return True 


@dp.errors_handler(exception=CancelHandler) 
async def message_not_modified_handler(update, exc): 
    return True


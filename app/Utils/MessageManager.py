from aiogram.types  import ParseMode 
from ..bot          import bot
from ..Static       import Vocabulary as Voc


class MessageManager():
    @staticmethod
    async def SendText(text, tg_user_id):
        resp = await bot.send_message(
                 tg_user_id, 
                 text,
                 parse_mode=ParseMode.MARKDOWN)
        return resp.message_id

    @staticmethod
    async def SendInlineKB(kb, kb_desc, tg_user_id):
        resp = await bot.send_message(
                 tg_user_id, 
                 kb_desc,
                 reply_markup=kb,
                 parse_mode=ParseMode.MARKDOWN)
        return resp.message_id

    @staticmethod
    async def Delete(message_id, tg_user_id):
        return await bot.delete_message(tg_user_id, message_id)

    @staticmethod
    async def SendDocument(document, tg_user_id):
        return await bot.send_document(
                chat_id=tg_user_id, 
                document=document)


class Send():
    @staticmethod
    async def NoTextInputWarning(tg_user_id):
        return await MessageManager.SendText(
                Voc.NoTextInput,
                tg_user_id)

    @staticmethod
    async def NoButtonPressWarning(tg_user_id):
        return await MessageManager.SendText(
                Voc.NoButtonInput,
                tg_user_id)

    @staticmethod
    async def NoCommandsInputWarning(tg_user_id):
        return await MessageManager.SendText(
                Voc.NoCommandsInput,
                tg_user_id)

    @staticmethod
    async def PromptForInput(tg_user_id):
        return await MessageManager.SendText(
                Voc.GimmeData,
                tg_user_id)

    @staticmethod
    async def TooLongInput(tg_user_id):
        return await MessageManager.SendText(
                Voc.TooLongInput,
                tg_user_id)


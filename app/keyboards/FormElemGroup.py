from aiogram.types  import InlineKeyboardMarkup, InlineKeyboardButton
from ..Utils        import CallbackTransformer, MessageManager
from ..Static       import Vocabulary as Voc


class FormElemGroup():
    def __init__(self, tg_user_id):
        self.tg_user_id = tg_user_id

    def AddElem(self, elem):
        raise NotImplementedError

    def Display(self, tg_user_id):
        raise NotImplementedError
      

class TextMessage(FormElemGroup):
    def __init__(self, tg_user_id):
        super().__init__(tg_user_id)
        self.type  = 'TEXT'
        self.texts = list() 

    def AddElem(self, elem):
        self.texts.append( {
            'text'      : elem['text'], 
            'mess_id'   : None, 
        } )

    async def Display(self):
        for text in self.texts:
            if text['mess_id']:
                await MessageManager.Delete(text['mess_id'],
                                            self.tg_user_id)
            id = await MessageManager.SendText(text['text'],
                                              self.tg_user_id)
            text['mess_id'] = id

    async def Hide(self):
        for text in self.texts:
            await MessageManager.Delete(text['mess_id'],
                                        self.tg_user_id)


class InlineKeyboard(FormElemGroup):
    def __init__(self, tg_user_id, kb_desc=None):
        super().__init__(tg_user_id)
        self.type = None
        self.kb   = InlineKeyboardMarkup(
                    row_width=2, 
                    resize_keyboard=True)
        self.kb_desc = kb_desc
        self.id      = None

    def AddElem(self, elem):
        if   not self.type:
            self.__AddType(elem)
        elif self.type != elem['type']:
            raise RuntimeError('Wrong element type for Inline Keyboard')
        self.kb.add(
            InlineKeyboardButton(
                text=self.__GetText(elem), 
                callback_data=CallbackTransformer.Join(
                    elem['type'], 
                    elem['id'], 
                    elem['cb'],
                    str(elem.get('d_id', '')))
            )
        )

    async def Display(self):
        id = await MessageManager.SendInlineKB(self.kb, 
                                              self.kb_desc,
                                              self.tg_user_id)
        self.id = id

    async def Hide(self):
        await MessageManager.Delete(self.id,
                                    self.tg_user_id)

    def __AddType(self, elem):
        self.type = elem['type']
        if not self.kb_desc:
            match(elem['type']):
                case 'FORM':
                    self.kb_desc = Voc.FormPrompt
                case 'D_FORM':
                    self.kb_desc = Voc.DynFormPrompt
                case 'BUTTON':
                    self.kb_desc = Voc.ButtonPrompt
                case 'S_CHOICE':
                    self.kb_desc = Voc.SingleChoicePrompt
                case 'M_CHOICE':
                    self.kb_desc = Voc.MultiChoisePrompt

    def HasStdKbDesc(self):
        match(self.kb_desc):
            case Voc.FormPrompt:
                return True
            case Voc.DynFormPrompt:
                return True
            case Voc.ButtonPrompt:
                return True
            case Voc.SingleChoicePrompt:
                return True
            case Voc.MultiChoisePrompt:
                return True
        return False

    def __GetText(self, elem):
        pref = ''
        if elem['completed']:
            pref = "✅ "
        return pref + elem['text']


from ..keyboards    import TextMessage, InlineKeyboard, Form
from ..Static       import Vocabulary as Voc 


class FormGroupFactory():
    @staticmethod
    def INIT():
        pass

    @staticmethod
    def Make(t, tg_user_id):
        if t == 'TEXT':
            return TextMessage(tg_user_id)
        return InlineKeyboard(tg_user_id)


class FormFactory():
    @staticmethod
    def INIT():
        pass

    @staticmethod
    def Make(form_description, tg_user_id):
        form        = Form(tg_user_id)
        prev_type   = None
        cur_group   = None 
        last_text   = None 

        for elem, next_elem in cur_and_next(form_description):
            if   elem['type'] == 'TEXT' and \
               next_elem and next_elem['type'] != 'TEXT':
                last_text = elem['text']
                continue

            if elem['type'] != prev_type:
                form.AddGroup(cur_group)
                prev_type = elem['type']
                if prev_type == 'TEXT':
                    cur_group = TextMessage(tg_user_id)
                else:
                    cur_group = InlineKeyboard(tg_user_id, last_text)
                    last_text = None
            cur_group.AddElem(elem)

        if hasattr(cur_group, 'kb_desc') and cur_group.HasStdKbDesc():
            cur_group.kb_desc = Voc.Navigation 
        form.AddGroup(cur_group)

        return form


def cur_and_next(l):
    from itertools import tee, islice, chain
    items, nexts = tee(l, 2)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(items, nexts)


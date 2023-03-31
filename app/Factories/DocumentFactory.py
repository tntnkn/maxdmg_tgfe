from aiogram.types import InputFile


class DocumentFactory():
    docgen = None

    @staticmethod
    def INIT(docgen):
        DocumentFactory.docgen = docgen

    @staticmethod
    def Make(contents):
        f_name = DocumentFactory.docgen.MakeDocument(
                contents['tags']).f_name
        file = InputFile(f_name, filename="Иск.docx")        
        DocumentFactory.docgen.DeleteDocument(f_name)
        return file


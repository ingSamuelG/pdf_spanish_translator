import os
from pypdf import PdfReader
from doc_creator.doc_creator import DocCreator

class PdfHandler:

    def __init__(self, file_path:str,file_name:str, translator):
        self.file_path = file_path
        self.file = open(file_path, 'rb')
        self.reader = PdfReader(self.file)
        self.file_name = file_name
        self.translator = translator

    def __translate(self,text):
        return self.translator.translate(text)

    def __close_file(self):
        self.file.close()
    
    def translate_page(self,page_num: int):
        text = self.reader.pages[page_num-1].extract_text()
        spanish = self.__translate(text)
        return spanish

    def translate_document_to_doc_file(self, doc_creator:DocCreator):
        number_of_pages = self.reader._get_num_pages()
        for page in range(27,36): # delete to read all 
            spanish_text =self.translate_page(page)
            doc_creator.create_page(text=spanish_text)
        self.__close_file()
        



            














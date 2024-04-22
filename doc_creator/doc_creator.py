from docx import Document


class DocCreator:
    def __init__(self, doc_name):
        self.document = Document()
        self.doc_name = doc_name

    def create_page(self, text:str):
        list_of_text = text.split("\n")
        print(f"crating page for doc")
        for para in list_of_text:
            self.document.add_paragraph(para)
        
        self.document.add_page_break()
    
    def save_doc(self):
        final_doc_name = self.doc_name + "_spanish.docx"
        self.document.save(final_doc_name)
    


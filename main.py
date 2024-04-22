import os
from pdf_handler.pdf_handler import PdfHandler
from doc_creator.doc_creator import DocCreator
from deep_translator import GoogleTranslator

def run_translate():
    translator = GoogleTranslator(source="en", target="es")
    file_path = "./files/NIST.SP.800-53r5.pdf"
    file_name = os.path.splitext(file_path)[0]
    new_docx = DocCreator(file_name)
    pdf = PdfHandler(file_path,file_name,translator)
    pdf.translate_document_to_doc_file(start_page=27,doc_creator=new_docx)   
    new_docx.save_doc() 

if __name__ == "__main__":
    run_translate()
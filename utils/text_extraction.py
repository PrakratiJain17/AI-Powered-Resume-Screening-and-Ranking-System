from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    """Extracts text from a PDF file."""
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
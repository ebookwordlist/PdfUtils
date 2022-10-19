from PyPDF2 import PdfReader
reader = PdfReader("Expert.Swift.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print(text)

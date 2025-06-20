import os
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID
from pdfminer.high_level import extract_text as pdf_extract
from docx import Document
from PIL import Image
import pytesseract

SCHEMA = Schema(
    path=ID(stored=True, unique=True),
    filename=TEXT(stored=True),
    content=TEXT,
    tags=TEXT(stored=True)
)

def get_text_from_file(filepath):
    ext = filepath.lower().split('.')[-1]
    try:
        if ext == 'txt':
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        elif ext == 'pdf':
            return pdf_extract(filepath)
        elif ext == 'docx':
            doc = Document(filepath)
            return "\n".join([p.text for p in doc.paragraphs])
        elif ext in ['png', 'jpg', 'jpeg']:
            return pytesseract.image_to_string(Image.open(filepath))
    except:
        return ""
    return ""

def build_index(dir_to_index="/home/faiza/Documents", index_dir="data/index"):
    if not os.path.exists(index_dir):
        os.makedirs(index_dir)
        ix = create_in(index_dir, SCHEMA)
    else:
        ix = open_dir(index_dir)

    writer = ix.writer()
    for root, _, files in os.walk(dir_to_index):
        for file in files:
            path = os.path.join(root, file)
            filename = file.lower()
            text = get_text_from_file(path)
            if text.strip():
                writer.update_document(path=path, filename=filename, content=text, tags="")
                print(f"Indexed: {path}")
    writer.commit()
    print("✅ Indexing complete.")

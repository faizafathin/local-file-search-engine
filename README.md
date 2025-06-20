# 🧠 Local File Search Engine with OCR and GUI

A lightweight Python-based desktop search engine that allows users to search through local `.pdf`, `.docx`, and `.txt` files using natural language queries. It uses OCR (Optical Character Recognition) to index scanned documents and provides a simple GUI to make searching seamless.

## ✨ Features

- 🔍 Full-text search of local files
- 📂 Supports PDF, Word (.docx), and plain text files
- 🧾 OCR support for scanned documents (PDF/Image-based)
- 🖼️ GUI built with Tkinter for easy usage
- ⚡ Fast indexing using Whoosh

## 🛠️ Tech Stack

- Python 3
- Whoosh
- PyMuPDF (fitz)
- python-docx
- pytesseract
- Tkinter

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/faizafathin/local-file-search-engine.git
cd local-file-search-engine

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

🚀 How to Use
bash
Copy
Edit
python indexer.py   # To index all files
python main.py      # To open the GUI and search

📁 Folder Structure
css
Copy
Edit
file_search_engine/
├── indexer.py
├── main.py
├── search.py
├── requirements.txt
├── README.md
└── data/

## 👩‍💻 Author

**Faiza Fathin**  
M.Sc. Bioinformatics | Python Developer | Linux Enthusiast  
🔗 [GitHub](https://github.com/faizafathin) 


# 🧠 Local File Search Engine with OCR and GUI

A lightweight Python-based desktop search engine that allows users to search through local documents (PDF, DOCX, TXT) — including scanned documents using OCR — with a user-friendly Tkinter-based GUI.

---

## ✨ Features

- 🔍 Full-text search of local files  
- 📂 Supports PDF, Word (.docx), and plain text files  
- 🧾 OCR support for scanned documents (PDF/Image-based)  
- 🖼️ GUI built with Tkinter for easy usage  
- ⚡ Fast indexing using Whoosh  

---

## 🛠️ Tech Stack

- Python 3  
- Whoosh (https://pypi.org/project/Whoosh/)  
- PyMuPDF (fitz)(https://pypi.org/project/PyMuPDF/)  
- python-docx (https://pypi.org/project/python-docx/)  
- pytesseract (https://pypi.org/project/pytesseract/)  
- Tkinter (https://wiki.python.org/moin/TkInter)

---

## 📦 Installation

### 📥 Clone the repo

```bash
git clone https://github.com/faizafathin/local-file-search-engine.git
cd local-file-search-engine

### 🐍 Create virtual environment

```bash
python3 -m venv venv
```

#### For Linux/macOS:
```bash
source venv/bin/activate
```

#### For Windows:
```bash
venv\Scripts\activate
```

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use

```bash
# Step 1: Index all files
python indexer.py

# Step 2: Launch the GUI
python main.py
```

---

## 📁 Folder Structure

```
file_search_engine/
├── indexer.py
├── main.py
├── search.py
├── requirements.txt
├── README.md
└── data/
```

---

## 👩‍💻 Author

**Faiza Fathin**  
M.Sc. Bioinformatics | Python Developer | Linux Enthusiast  
🔗 [GitHub](https://github.com/faizafathin)

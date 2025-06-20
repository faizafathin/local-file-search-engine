import tkinter as tk
from tkinter import messagebox
from search import search

def do_search():
    query = entry.get()
    if not query.strip():
        messagebox.showwarning("Empty", "Please enter a search term.")
        return
    results = search(query)
    listbox.delete(0, tk.END)
    if not results:
        listbox.insert(tk.END, "No results found.")
    for r in results:
        listbox.insert(tk.END, r["path"])

# GUI setup
root = tk.Tk()
root.title("🔍 Local File Search Engine")

entry = tk.Entry(root, width=60)
entry.pack(pady=10)

btn = tk.Button(root, text="Search", command=do_search)
btn.pack()

listbox = tk.Listbox(root, width=100, height=20)
listbox.pack(pady=10)

root.mainloop()

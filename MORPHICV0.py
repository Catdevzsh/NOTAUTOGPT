import tkinter as tk
from tkinter import filedialog, Text, ttk
import os

root = tk.Tk()
root.title("Morphic Compiler IDE")

# Create the layout
header_frame = ttk.Frame(root, padding=5)
header_frame.grid(row=0, column=0, sticky="WENS")
editor_frame = ttk.Frame(root, padding=5)
editor_frame.grid(row=1, column=0, sticky="WENS")
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
import tkinter as tk
from tkinter import messagebox, simpledialog
import os

def save_api_key(api_key):
    documents_path = os.path.expanduser('~\\Documents')
    file_path = os.path.join(documents_path, 'openai_api_key.txt')
    with open(file_path, 'w') as f:
        f.write(api_key)

def request_api_key():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo('GPT-4 Compiler', 'Please provide your OpenAI API key.')
    api_key = simpledialog.askstring('API Key', 'Enter your OpenAI API key:')
    if api_key:
        save_api_key(api_key)
        messagebox.showinfo('GPT-4 Compiler', 'API key saved successfully.')
    root.quit()

request_api_key()
 
import os
from pathlib import Path

def save_api_key_to_morphic_memory(key):
    with open("morphic_memory.txt", "w") as f:
        f.write(key)

def read_api_key_from_file(file_path):
    with open(file_path, "r") as f:
        key = f.read()
    return key.strip()

def store_api_key_permanently():
    documents_path = str(Path.home() / "Documents")
    api_key_file = os.path.join(documents_path, "openai_key.txt")

    if os.path.exists(api_key_file):
        api_key = read_api_key_from_file(api_key_file)
        save_api_key_to_morphic_memory(api_key)
        print("API key has been saved to morphic memory.")
    else:
        print("API key file not found in Documents.")

store_api_key_permanently()

# HUD
def update_hud():
    # Add the code to update the HUD here
    hud_label.config(text="Morphic Compiler IDE")
    root.after(100, update_hud)

hud_label = ttk.Label(header_frame, text="")
hud_label.pack(side="right")
root.after(100, update_hud)

# File management
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".morphic")

    if file_path:
        editor.delete("1.0", "end")
        with open(file_path, "r") as file:
            editor.insert("1.0", file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".morphic")

    if file_path:
        with open(file_path, "w") as file:
            file.write(editor.get("1.0", "end"))

def compile_file():
    # Add the code to compile the Morphic code here
    pass

# Menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

compile_menu = tk.Menu(menu)
menu.add_cascade(label="Compile", menu=compile_menu)
compile_menu.add_command(label="Compile", command=compile_file)

# Editor
editor = Text(editor_frame, wrap="none")
editor.grid(row=0, column=0, sticky="WENS")
editor_frame.columnconfigure(0, weight=1)
editor_frame.rowconfigure(0, weight=1)

# Scrollbars
x_scroll = ttk.Scrollbar(editor_frame, orient="horizontal", command=editor.xview)
x_scroll.grid(row=1, column=0, sticky="WE")
y_scroll = ttk.Scrollbar(editor_frame, orient="vertical", command=editor.yview)
y_scroll.grid(row=0, column=1, sticky="NS")
editor.config(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

editor.bind("<Any-KeyRelease>", lambda _: root.after(100, update_hud))

root.mainloop()

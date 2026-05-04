
# Online Python - IDE, Editor, Compiler, Interpreter
import tkinter as tk

from tkinter import messagebox

import random

import json

import os

# --- Данные ---

quotes = [

    {"text": "Жизнь прекрасна", "author": "Автор 1", "theme": "жизнь"},

    {"text": "Учись каждый день", "author": "Автор 2", "theme": "обучение"},

    {"text": "Никогда не сдавайся", "author": "Автор 3", "theme": "мотивация"}

]

history = []

FILE_NAME = "history.json"

# --- Загрузка истории ---

if os.path.exists(FILE_NAME):

    with open(FILE_NAME, "r", encoding="utf-8") as f:

        try:

            history = json.load(f)

        except:

            history = []

# --- Функции ---

def generate_quote():

    if not quotes:

        messagebox.showwarning("Ошибка", "Нет цитат")

        return

    quote = random.choice(quotes)

    text = f"{quote['text']} — {quote['author']} ({quote['theme']})"

    

    label.config(text=text)

    

    history.append(quote)

    update_history()

def update_history(filtered=None):

    listbox.delete(0, tk.END)

    

    data = filtered if filtered else history

    

    for q in data:

        listbox.insert(tk.END, f"{q['text']} — {q['author']}")

def save_history():

    with open(FILE_NAME, "w", encoding="utf-8") as f:

        json.dump(history, f, ensure_ascii=False, indent=4)

def filter_quotes():

    author = entry_author.get().lower()

    theme = entry_theme.get().lower()

    filtered = []

    for q in history:

        if (author in q["author"].lower()) and (theme in q["theme"].lower()):

            filtered.append(q)

    update_history(filtered)

def add_quote():

    text = entry_text.get()

    author = entry_new_author.get()

    theme = entry_new_theme.get()

    if not text or not author or not theme:

        messagebox.showerror("Ошибка", "Все поля должны быть заполнены")

        return

    quotes.append({"text": text, "author": author, "theme": theme})

    entry_text.delete(0, tk.END)

    entry_new_author.delete(0, tk.END)

    entry_new_theme.delete(0, tk.END)

    messagebox.showinfo("Успех", "Цитата добавлена")

def on_closing():

    save_history()

    root.destroy()

# --- GUI ---

root = tk.Tk()

root.title("Random Quote Generator")

root.geometry("500x600")

label = tk.Label(root, text="Нажми кнопку", wraplength=400)

label.pack(pady=10)

btn = tk.Button(root, text="Сгенерировать цитату", command=generate_quote)

btn.pack(pady=10)

# История

listbox = tk.Listbox(root, width=60, height=10)

listbox.pack(pady=10)

# Фильтр

tk.Label(root, text="Фильтр по автору").pack()

entry_author = tk.Entry(root)

entry_author.pack()

tk.Label(root, text="Фильтр по теме").pack()

entry_theme = tk.Entry(root)

entry_theme.pack()

filter_btn = tk.Button(root, text="Фильтровать", command=filter_quotes)

filter_btn.pack(pady=5)

# Добавление цитаты

tk.Label(root, text="Добавить цитату").pack(pady=10)

entry_text = tk.Entry(root, width=40)

entry_text.pack()

entry_text.insert(0, "Текст")

entry_new_author = tk.Entry(root)

entry_new_author.pack()

entry_new_author.insert(0, "Автор")

entry_new_theme = tk.Entry(root)

entry_new_theme.pack()

entry_new_theme.insert(0, "Тема")

add_btn = tk.Button(root, text="Добавить", command=add_quote)

add_btn.pack(pady=5)

root.protocol("WM_DELETE_WINDOW", on_closing)

update_history()

root.mainloop()

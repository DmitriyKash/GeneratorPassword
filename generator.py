import tkinter as tk
from tkinter import ttk

from app.app_func import generate_passwords, save_passwords


def generate_and_save_passwords():
    """
    Generates and saves passwords based on the length and count entered in the GUI.

    Parameters:
        None

    Returns:
        None
    """
    length = int(length_entry.get())
    count = int(count_entry.get())
    passwords = generate_passwords(length, count, use_letters.get(), use_digits.get(), use_punctuation.get())
    save_passwords(passwords)


# Створення вікна
window = tk.Tk()
window.title("Генератор паролів")

# Макет
frame = ttk.Frame(window)
frame.pack(padx=10, pady=10)

# Довжина пароля
ttk.Label(frame, text="Довжина пароля:").grid(row=0, column=0, sticky=tk.W)
length_entry = ttk.Entry(frame)
length_entry.grid(row=0, column=1)
length_entry.insert(0, "12")

# Кількість паролів
ttk.Label(frame, text="Кількість паролів:").grid(row=1, column=0, sticky=tk.W)
count_entry = ttk.Entry(frame)
count_entry.grid(row=1, column=1)
count_entry.insert(0, "1")

# Прапорці для вибору типів символів
use_letters = tk.BooleanVar(value=True)
chk_letters = ttk.Checkbutton(frame, text="Використовувати букви", variable=use_letters)
chk_letters.grid(row=2, column=0, columnspan=2, sticky=tk.W)

use_digits = tk.BooleanVar(value=True)
chk_digits = ttk.Checkbutton(frame, text="Використовувати цифри", variable=use_digits)
chk_digits.grid(row=3, column=0, columnspan=2, sticky=tk.W)

use_punctuation = tk.BooleanVar(value=True)
chk_punctuation = ttk.Checkbutton(frame, text="Використовувати спецсимволи", variable=use_punctuation)
chk_punctuation.grid(row=4, column=0, columnspan=2, sticky=tk.W)

# Кнопка генерації
generate_button = ttk.Button(frame, text="Генерувати", command=generate_and_save_passwords)
generate_button.grid(row=5, column=0, columnspan=2, pady=5)


# Запуск головного циклу
window.mainloop()

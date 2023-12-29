import random
import string
from tkinter import messagebox


def generate_passwords(length, count, use_letters, use_digits, use_punctuation):
    """
    Generate passwords based on specified criteria.

    Parameters:
        length (int): The desired length of each password.
        count (int): The number of passwords to generate.
        use_letters (bool): Whether to include letters in the passwords.
        use_digits (bool): Whether to include digits in the passwords.
        use_punctuation (bool): Whether to include punctuation marks in the passwords.

    Returns:
        list: A list of generated passwords.

    Raises:
        None.

    Usage:
        passwords = generate_passwords(8, 10, True, False, True)
    """
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if characters:
        return ["".join(random.choice(characters) for _ in range(length)) for _ in range(count)]
    else:
        messagebox.showinfo("Помилка", "Виберіть тип символів")
        return []


# Функція для збереження паролів у файл
def save_passwords(passwords):
    """
    Saves the passwords to a file.

    Parameters:
    - passwords (list): A list of passwords to be saved.

    Returns:
    - None

    Raises:
    - None
    """
    if passwords:
        with open("passwords.txt", "w") as file:
            for password in passwords:
                file.write(password + "\n")
        messagebox.showinfo("Генерація завершена", f"{len(passwords)} паролів збережено у 'passwords.txt'")

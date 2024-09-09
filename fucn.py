import random
import string

def generate_password(length, use_caps, use_numbers, use_specials):
    # Базовые символы
    chars = string.ascii_lowercase

    # Если Caps Lock активен, добавляем заглавные буквы
    if use_caps:
        chars += string.ascii_uppercase

    # Если Numbers активен, добавляем цифры
    if use_numbers:
        chars += string.digits

    # Если Special Sign активен, добавляем специальные символы
    if use_specials:
        chars += string.punctuation

    # Генерация пароля указанной длины
    password = ''.join(random.choice(chars) for _ in range(length))

    return password

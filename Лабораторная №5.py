import re

def check_postal_code(postal_code):
    pattern = r'^\d{5}$'  # Регулярное выражение для почтового индекса из пяти цифр

    if not re.match(pattern, postal_code):
        raise ValueError("Неверный формат почтового индекса")

    return True

# Пример использования
postal_codes = ["12345", "54321", "987654", "abcde", "123456", "5432a"]

for postal_code in postal_codes:
    try:
        if check_postal_code(postal_code):
            print(f"{postal_code} - это почтовый индекс из пяти цифр.")
    except ValueError as e:
        print(f"Ошибка: {e}")

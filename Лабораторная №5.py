def is_zip_code(input_string):
    # Проверяем длину строки
    if len(input_string) != 5:
        return False

    # Проверяем, что все символы в строке являются цифрами
    if not input_string.isdigit():
        return False

    # Если прошли обе проверки, возвращаем True
    return True

def validate_zip_code(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Аргумент должен быть строкой")

    if is_zip_code(input_string):
        return input_string
    else:
        raise ValueError("Некорректный почтовый индекс")

try:
    zip_code = validate_zip_code("12345-")
    print("Почтовый индекс:", zip_code)
except ValueError as ve:
    print("Ошибка:", ve)
except TypeError as te:
    print("Ошибка:", te)


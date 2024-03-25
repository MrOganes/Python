import sqlite3
import cgi
import json
import xml.etree.ElementTree as ET

# Подключение к базе данных SQLite
conn = sqlite3.connect('./software_database.db')
c = conn.cursor()

# Создание таблицы, если её ещё нет
c.execute('''CREATE TABLE IF NOT EXISTS Developers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                specialization TEXT NOT NULL
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Projects (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                start_date DATE,
                end_date DATE,
                developer_id INTEGER,
                FOREIGN KEY (developer_id) REFERENCES Developers(id)
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Clients (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                contact_person TEXT,
                email TEXT
             )''')

# Получение данных из формы
form = cgi.FieldStorage()


# Функция для импорта данных из JSON
def import_json(data):
    json_data = json.loads(data)
    for entry in json_data:
        if 'Specialization' in entry.keys():  # Проверяем, что JSON содержит поле 'ID', чтобы определить тип данных
            c.execute("INSERT INTO Developers (name, specialization) VALUES (?, ?)", (entry['Name'], entry['Specialization']))
        elif 'Start Date' in entry.keys():  # Это записи о проектах
            c.execute("INSERT INTO Projects (name, description, start_date, end_date, developer_id) VALUES (?, ?, ?, ?, ?)",
                (entry['Name'], entry['Description'], entry['Start Date'], entry['End Date'], entry['Developer ID']))
        elif 'Email' in entry.keys():  # Это записи о клиентах
            c.execute("INSERT INTO Clients (name, contact_person, email) VALUES (?, ?, ?)",
                      (entry['Name'], entry['Contact Person'], entry['Email']))

# Функция для импорта данных из XML
def import_xml(data):
    root = ET.fromstring(data)
    for entry in root.findall('Entry'):
        data = {}
        for field in entry:
            data[field.tag.replace("_", " ")] = field.text
        if 'Specialization' in data.keys():  # Проверяем, что JSON содержит поле 'ID', чтобы определить тип данных
            c.execute("INSERT INTO Developers (name, specialization) VALUES (?, ?)", (data['Name'], data['Specialization']))
        elif 'Start Date' in data.keys():  # Это записи о проектах
            c.execute("INSERT INTO Projects (name, description, start_date, end_date, developer_id) VALUES (?, ?, ?, ?, ?)",
                (data['Name'], data['Description'], data['Start Date'], data['End Date'], data['Developer ID']))
        elif 'Email' in data.keys():  # Это записи о клиентах
            c.execute("INSERT INTO Clients (name, contact_person, email) VALUES (?, ?, ?)",
                      (data['Name'], data['Contact Person'], data['Email']))

# Получение данных о типе и файле
data_type = form.getvalue('data_type')
file_data = form.getvalue('file_input')

# Определение типа файла и импорт данных
if data_type == 'json':
    import_json(file_data)
elif data_type == 'xml':
    import_xml(file_data)

# Подтверждение изменений и закрытие соединения с базой данных
conn.commit()
conn.close()
print("Content-type: text/html; charset=utf-8\n")
print("<html>")
print("<body>")
print("Ваши данные приняты к рассмотрению.")
print("<body>")
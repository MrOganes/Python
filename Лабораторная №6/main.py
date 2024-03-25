import sqlite3

# Создание соединения с базой данных
conn = sqlite3.connect('software_database.db')
c = conn.cursor()

# Создание таблиц
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

conn.commit()

# Вставка данных в таблицы
c.execute("INSERT INTO Developers (name, specialization) VALUES (?, ?)", ('Элизбаров Оганес', 'Разработчик'))
c.execute("INSERT INTO Developers (name, specialization) VALUES (?, ?)", ('Деркач Андрей', 'Стажер 1С'))

c.execute("INSERT INTO Projects (name, description, start_date, end_date, developer_id) VALUES (?, ?, ?, ?, ?)",
          ('Сайт', 'Разработка сайта', '2024-01-01', '2024-06-30', 1))
c.execute("INSERT INTO Projects (name, description, start_date, end_date, developer_id) VALUES (?, ?, ?, ?, ?)",
          ('1С', 'Настройка 1С базы', '2024-02-01', '2024-08-31', 2))

c.execute("INSERT INTO Clients (name, contact_person, email) VALUES (?, ?, ?)",
          ('Магнит', 'Сергей Галицкий', 'sergey@example.com'))

c.execute("INSERT INTO Clients (name, contact_person, email) VALUES (?, ?, ?)",
          ('КубГУ', 'Михаил Астапов', 'kubsu@example.com'))


# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()


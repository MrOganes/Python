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
conn.close()
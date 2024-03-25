#!/usr/bin/env python3

import sqlite3
import json
import xml.etree.ElementTree as ET

print("Content-type: text/html; charset=utf-8\n")
print("<html>")
print("<head>")
print("<link rel='stylesheet' type='text/css' href='../style2.css'>")
print("</head>")
print("<body>")

# Создание соединения с базой данных
conn = sqlite3.connect('./software_database.db')
c = conn.cursor()

# Запрос на выборку всех записей из таблицы Developers
c.execute("SELECT * FROM Developers")
developers = c.fetchall()

# Запрос на выборку всех записей из таблицы Projects
c.execute("SELECT * FROM Projects")
projects = c.fetchall()

# Запрос на выборку всех записей из таблицы Clients
c.execute("SELECT * FROM Clients")
clients = c.fetchall()

# Генерация HTML страницы
print("<h1>Developers</h1>")
print("<table border='1'>")
print("<tr><th>ID</th><th>Name</th><th>Specialization</th></tr>")
for developer in developers:
    print("<tr>")
    print("<td>{}</td>".format(developer[0]))
    print("<td>{}</td>".format(developer[1]))
    print("<td>{}</td>".format(developer[2]))
    print("</tr>")
print("</table>")

print("<h1>Projects</h1>")
print("<table border='1'>")
print("<tr><th>ID</th><th>Name</th><th>Description</th><th>Start Date</th><th>End Date</th><th>Developer ID</th></tr>")
for project in projects:
    print("<tr>")
    print("<td>{}</td>".format(project[0]))
    print("<td>{}</td>".format(project[1]))
    print("<td>{}</td>".format(project[2]))
    print("<td>{}</td>".format(project[3]))
    print("<td>{}</td>".format(project[4]))
    print("<td>{}</td>".format(project[5]))
    print("</tr>")
print("</table>")

print("<h1>Clients</h1>")
print("<table border='1'>")
print("<tr><th>ID</th><th>Name</th><th>Contact Person</th><th>Email</th></tr>")
for client in clients:
    print("<tr>")
    print("<td>{}</td>".format(client[0]))
    print("<td>{}</td>".format(client[1]))
    print("<td>{}</td>".format(client[2]))
    print("<td>{}</td>".format(client[3]))
    print("</tr>")
print("</table>")

# Закрытие соединения с базой данных
conn.close()

# Создание словарей для таблиц
developers_dict = [{"ID": row[0], "Name": row[1], "Specialization": row[2]} for row in developers]
projects_dict = [{"ID": row[0], "Name": row[1], "Description": row[2], "Start Date": row[3], "End Date": row[4], "Developer ID": row[5]} for row in projects]
clients_dict = [{"ID": row[0], "Name": row[1], "Contact Person": row[2], "Email": row[3]} for row in clients]

developers_json = json.dumps(developers_dict, ensure_ascii=False)
projects_json = json.dumps(projects_dict, ensure_ascii=False)
clients_json = json.dumps(clients_dict, ensure_ascii=False)

# Создание файлов и запись в них данных JSON с указанием кодировки UTF-8
with open('developers.json', 'w', encoding='utf-8') as f:
    f.write(developers_json)

with open('projects.json', 'w', encoding='utf-8') as f:
    f.write(projects_json)

with open('clients.json', 'w', encoding='utf-8') as f:
    f.write(clients_json)


def save_xml(data, filename):
    root = ET.Element("Data")

    for item in data:
        entry = ET.SubElement(root, "Entry")
        for key, value in item.items():
            ET.SubElement(entry, key.replace(" ", "_")).text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

# Преобразование в XML строку
save_xml(developers_dict, 'developers.xml')
save_xml(projects_dict, 'projects.xml')
save_xml(clients_dict, 'clients.xml')

# Добавление кнопок для скачивания файлов
print("<h2>Download JSON and XML Files:</h2>")
print("<a href='/developers.json' download><button>Download Developers JSON</button></a>")
print("<a href='/projects.json' download><button>Download Projects JSON</button></a>")
print("<a href='/clients.json' download><button>Download Clients JSON</button></a>")
print("<br>")
print("<a href='/developers.xml' download><button>Download Developers XML</button></a>")
print("<a href='/projects.xml' download><button>Download Projects XML</button></a>")
print("<a href='/clients.xml' download><button>Download Clients XML</button></a>")

print("<h2>Import JSON or XML Data:</h2>")
print("<form action='/cgi-bin/import_date.py' method='post' enctype='multipart/form-data'>")
print("<label for='data_type'>Select Data Type:</label>")
print("<select id='data_type' name='data_type'>")
print("<option value='json'>JSON</option>")
print("<option value='xml'>XML</option>")
print("</select>")
print("<label for='file_input'>Choose File:</label>")
print("<input type='file' id='file_input' name='file_input' accept='.json,.xml' required>")
print("<button type='submit'>Import Data</button>")
print("</form>")

print("</body></html>")

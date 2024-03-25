#!/usr/bin/env python3
print("Content-type: text/html; charset=utf-8\n")
print("<html><body>")
print("<h1>Form Data Received:</h1>")

import cgi
import sqlite3

# Получение данных из формы
form = cgi.FieldStorage()
name = form.getvalue('name')
specialization = form.getvalue('specialization')

project_name = form.getvalue('project-name')
project_description = form.getvalue('project-description')
start_date = form.getvalue('start-date')
end_date = form.getvalue('end-date')

client_organization = form.getvalue('client-organization')
client_representative = form.getvalue('client-representative')
client_email = form.getvalue('client-email')

# Соединение с базой данных
conn = sqlite3.connect('software_database.db')
c = conn.cursor()

# Вставка данных в таблицу Developers
c.execute("INSERT INTO Developers (name, specialization) VALUES (?, ?)", (name, specialization))
c.execute("INSERT INTO Projects (name, description, start_date, end_date, developer_id) VALUES (?, ?, ?, ?, ?)",
          (project_name, project_description, start_date, end_date, 1))
c.execute("INSERT INTO Clients (name, contact_person, email) VALUES (?, ?, ?)",
          (client_organization, client_representative, client_email))
conn.commit()
conn.close()

# Вывод информации о том, что данные были успешно сохранены
print("<ul>")
print("<li>Data successfully saved for developer:</li>")
print("<li>Name: {}</li>".format(name))
print("<li>Specialization: {}</li>".format(specialization))
print("<li>Project name: {}</li>".format(project_name))

print("<li>Project description: {}</li>".format(project_description))
print("<li>Start date: {}</li>".format(start_date))
print("<li>End date: {}</li>".format(end_date))

print("<li>Client organization: {}</li>".format(client_organization))
print("<li>Client_representative: {}</li>".format(client_representative))
print("<li>Client email: {}</li>".format(client_email))

print("</ul>")
print("</body></html>")

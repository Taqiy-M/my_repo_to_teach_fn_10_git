password = "qwerty12345"

import sqlite3

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QApplication, QPushButton

a = sqlite3.connect('mening_bazam.db')
k = a.cursor()
# k.execute("""CREATE TABLE IF NOT EXISTS Ustoz (
#         id INTEGER,
#         ism TEXT,
#         fan TEXT,
#         yil INTEGER,
#         PRIMARY KEY (id)
#         );""")
# a.commit()
# a.close()
lim = 20
off = 513
q = f"SELECT * FROM Student LIMIT {lim} OFFSET {off}"
k.execute(q)
# print(k.fetchall())

# print(k.fetchmany(20))
# print(k.fetchmany(10))
# print(k.fetchmany(10))
# print(k.fetchmany(10))
# print(k.fetchmany(10))
# print(k.fetchmany(10))













# ########################


# for i in k.fetchall():
#     print(i[0], "Univer==>"+i[1])



















# row = k.fetchone()
# while row is not None:
#     print("Name:", row[0])
#     print("Univer:", row[1])
#     row = k.fetchone()

# ######################
# cursor.execute("SELECT name, age FROM your_table")
# rows = cursor.fetchall()
# for row in rows:
#     print("Name:", row[0])
#     print("Age:", row[1])
#
# ########################
# cursor.execute("SELECT name, age FROM your_table")
# rows = cursor.fetchmany(2)  # Fetch the first 2 rows
# while rows:
#     for row in rows:
#         print("Name:", row[0])
#         print("Age:", row[1])
#     rows = cursor.fetchmany(2)  # Fetch the next 2 rows
#
#
#
#
#
#
#
# #########pagination
# import sqlite3
#
# conn = sqlite3.connect('your_database.db')
# cursor = conn.cursor()
#
# page_size = 10
# current_page = 2  # Change this value to navigate to different pages
# offset = (current_page - 1) * page_size
#
# cursor.execute(f"SELECT * FROM your_table LIMIT {page_size} OFFSET {offset}")
# rows = cursor.fetchmany(page_size)
#
# for row in rows:
#     print(row)
#
# conn.close()
#
#
#
#
#
#
#
#
# # pip install mysql-connector-python
# import mysql.connector
# #
# # # Database connection parameters
# # db_config = {
# #     "host": "localhost",
# #     "user": "root",
# #     "password": "12345",
# #     "database": "mening_bazam"
# # }
# #
# # # Connect to the MySQL database
# # conn = mysql.connector.connect(host="localhost",
# #                                user="root",
# #                                password="12345",
# #                                database="mening_bazam")
# #
#
#
#
#
#
#
# # # Create a cursor
# # cursor = conn.cursor()
# #
# # # Execute SQL queries and commands
# # cursor.execute("SELECT * FROM your_table")
# # result = cursor.fetchall()
# # for row in result:
# #     print(row)
# #
# # # Commit changes (if needed)
# # # conn.commit()
# #
# # # Close the connection
# # conn.close()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

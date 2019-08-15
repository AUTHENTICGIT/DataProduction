#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sqlite3
from faker import Faker

conn = sqlite3.connect(r'D:\\DataBases\\数据库\\sqlite\\删除记录、字段、表测试\\table_del.db')
print("Opened database successfully")

cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'delete_tab'")
if not cur.fetchone():
    conn.execute('''CREATE TABLE delete_tab
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    country TEXT,
    state TEXT,
    city TEXT,
    address TEXT,
    postcode TEXT,
    latitude REAL,
    longitude REAL,
    phoneNumber TEXT,
    birthday DATE,
    email TEXT
    );''')
    print("Table created successfully")

fake = Faker()

# 批量录入i*j条记录
i = 0
while i < 1:
    sql = 'INSERT INTO delete_tab (name, country, state, city, address, postcode, latitude, longitude, phoneNumber, birthday, email) VALUES (?,?,?,?,?,?,?,?,?,?,?);'
    data = []
    j = 0
    while j < 500:
        # sql = sql + '(?,?,?,?,?,?,?,?,?,?,?),'
        data.append((
            fake.name(), fake.country(), fake.state(), fake.city(), fake.address(), fake.postcode(),
            float(fake.latitude()),
            float(fake.longitude()), fake.phone_number(), fake.date(), fake.email()))
        j = j + 1
    sql = sql[:-1] + ';'
    cur.executemany(sql, data)
    i = i + 1

conn.commit()
print('Table inserted successfully!')
# cur.execute('SELECT  * FROM person')
# print(cur.fetchall())
conn.close()
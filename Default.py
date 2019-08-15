import sqlite3
from faker import Faker

conn = sqlite3.connect(r'D:\\DataBases\\数据库\\sqlite\\亲和性测试\\test_blob.db')
print("Opened database successfully")

cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'file_binary'")
if not cur.fetchone():
    conn.execute('''CREATE TABLE file_binary
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    binary BLOB
    );''')
    print("Table created successfully")

# 初始化, 默认情况是en_US, 代表美式英文, zh-CN代表使用中国版
fake = Faker(locale='zh_CN')

# i=1
# while(i<=1000):
#     country = '\'' + fake.country() + '\''
#     sql = 'UPDATE first_end_col SET country=' + country + ' WHERE id=' + str(i) + ';'
#     print(sql)
#     cur.execute(sql)
#     i = i + 1
# conn.commit()
# 批量录入i*j条记录
i = 0
while i < 1:
    sql = 'INSERT INTO file_binary (filename, binary) VALUES (?,?);'
    data = []
    j = 0
    while j < 99:
        # sql = sql + '(?,?,?,?,?,?,?,?,?,?,?),'
        data.append((
            fake.file_name(), fake.binary(length=1048576)))
        j = j + 1
    sql = sql[:-1] + ';'
    cur.executemany(sql, data)
    i = i + 1

conn.commit()
print('Table inserted successfully!')
conn.close()
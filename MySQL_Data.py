import pymysql
from faker import Faker

password = input('Enter your database password:')
conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd=password, db='information_schema')
conn2 = pymysql.connect(host='localhost', port=3306, user='root', passwd=password, db='quantity_test', charset='utf8')
print("Opened database successfully!",conn1,conn2)

cur1 = conn1.cursor()
cur1.execute("SELECT table_name FROM tables WHERE table_schema = 'quantity_test' AND table_type LIKE '%table%' AND table_name = 'template'")
cur2 = conn2.cursor()

if not cur1.fetchone():
    cur2.execute('''CREATE TABLE template
    (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(10),
    ssn VARCHAR(20),
    phone VARCHAR(11),
    creditcard VARCHAR(20),
    job VARCHAR(50),
    salary DECIMAL(10,2),
    creditscore tinyint,
    city varchar(10)
    )
    ''')
    print("Table created successfully!")

fake = Faker(locale='zh_CN')

i= 0
while i < 2:
    sql = "INSERT INTO template (name, ssn, phone, creditcard, job, salary, creditscore, city) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
    data = []
    j = 0
    while j < 5:
        # sql = sql + '(?,?,?), 姓名，身份证号，电话，银行卡，工作，收入，信用，城市'
        data.append((
            fake.name(),
            fake.ssn(),
            fake.phone_number(),
            fake.credit_card_number(),
            fake.job(),
            fake.pyint(min_value=0, max_value=20000, step=1000),
            fake.pyint(min_value=-10, max_value=100, step=1),
            fake.city()
        ))
        j = j + 1
    sql = sql[:-1] + ';'
    cur2.executemany(sql, data)
    print('{} inserted!'.format((i + 1) * j))
    i = i + 1

conn2.commit()
print('Table inserted successfully!')
conn2.close()
conn1.close()
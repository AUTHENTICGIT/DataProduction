import json
import psycopg2

conn = psycopg2.connect(host="localhost", port=5432, user="postgres", password="postgres", database="postgres")
print("Opened database successfully!",conn)
cur = conn.cursor()

id = 1
sentence = ['测试句子1', '测试句子2']
insert_sql = "INSERT INTO jsonb_test (id, jsonb_) VALUES (%s, %s);"
conn.cursor().execute(insert_sql, (id, json.dumps(sentence)))

conn.commit()
print('Table inserted successfully!')
conn.close()
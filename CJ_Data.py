import pymysql
from faker import Faker
import random

# 生成随机节点树
def getData(line):
    fake = Faker(locale='zh_CN')
    id = range(1, line+1)
    # 根节点(1,0,,,)
    # data = [(1,0,fake.name(),fake.phone_number(),fake.ssn())]
    data = []
    for i in id:
        data.append((
            i,
            random.randint(0, line-1),
            fake.name(),
            fake.phone_number(),
            fake.ssn()
        ))
    return data

# 生成num个节点c级关系
def getData2(num,c):
    list = [(1,)]
    n = 1
    ready = 1
    for i in range(2, c+1):
        if i < c:
            n = random.choice(range(1, num-ready-(c-i)))
        else:
            n = num - ready
        list.append(tuple(range(ready+1, ready+1+n)))   #[(),(),()]
        ready = ready + n
    print(list)

    fake = Faker(locale='zh_CN')
    # 根节点
    table = [(1, 0, fake.name(), fake.phone_number(), fake.ssn())]
    j = 0
    for node in list[1:]:
        for id in node:
            pid = random.choice(list[j])
            table.append((
                id,
                pid,
                fake.name(),
                fake.phone_number(),
                fake.ssn()
            ))
        j = j + 1
    return table

def insert_by_mysql(table):
    # 建立连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='pydata_01', charset='utf8')
    cur = conn.cursor()
    try:
        # 批量插入
        sql = '''INSERT INTO base05 VALUES(%s, %s, %s, %s, %s)'''
        res = cur.executemany(sql, table)
        conn.commit()
        print(res)
        print('[insert_by_msyql executemany] toal:', len(table))
    except Exception as e:
        print('[insert error]:', e)
        conn.rollback()
    cur.close()
    conn.close()
    return(Exception)

def main():
    # table = getData(50)
    number = int(input('请指定总结点数：'))
    rank = int(input('请指定生成层级数：'))
    table = getData2(number, rank)
    trigger1 = input('是否写入数据库[Y/N]：')
    while(trigger1.lower() == 'n'):
        trigger2 = input('是否重新生成数据[Y/N]：')
        if(trigger2.lower() == 'y'):
            table = getData2(number, rank)
            trigger1 = input('是否写入数据库[Y/N]：')
        else:
            break
    if(trigger1.lower() =='y'):
        if(insert_by_mysql(table)):
            print('写入失败！')
        else:
            print('写入成功！')
    else:
        print('未写入，结束程序！')

if __name__ == '__main__':
    main()

import pymysql
from faker import Faker
import random
from time import time
from datetime import datetime

conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='123456', db='dbg80', charset='utf8')
print("Opened database successfully!",conn)

cur = conn.cursor()

fake = Faker(locale='zh_CN')
browser = ['Internet Explorer11.0','Safari 6533.18.5','Unknow browser','FireFox 3.5.2','Chrome 13.1','Safari 525.20.1/UCWEB7.9.4.145/139/32488']
system = ['Windows NT','Windows XP','Windows 2000','Unknow', 'Windows Vista']
language = ['zh-cn','en-US','en-uk','en-us,en,zh-cn','zh-cn,zh-hk,zh-tw,en','en']
domain = ['http://www.bjhgww.com','http://hap1.ucweb.com.cn:8040','http://61.131.89.155','http://218.108.240.22:3438','http://www.google.cn.www.google.com.hk.www.baidu.com.www.bing.com.www.soso.com','']
path = ['','/','/user.php?act=logout','/s?wd=%B0%D9%BC%D2%BA%CD%B9%BA%CE%EF&opt-webpage=on&ie=gbk','/user.php?act=account_log','/s?word=%B0%D9%BC%D2%BA%CD%B9%BA%CE%EF%CD%F8&tn=sitehao123&f=3']
url = ['/index.php','/user.php','/ips_respond.php','/dousermoney.php']

i = 0
while i < 20000:
    sql = "INSERT INTO wj_stats (access_time, ip_address, visit_times, browser, sys, language, area, referer_domain, referer_path, access_url) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    data = []
    j = 0
    while j < 100:
        # sql = sql + '(?,?,?), xly_id_dbf ， xly_状态_dbf ， xly_偏移位置_dbf ， xly_文件号_dbf ， access_time ， ip_address ， visit_times ， browser ， system ， language ， area ， referer_domain ， referer_path ， access_url ' 
        data.append((
            int(time()),                                            # access_time
            fake.ipv4(),                                            # ip_address
            fake.pyint(min_value=0, max_value=1200, step=2),        # visit_times
            random.choice(browser),                                 # browser
            random.choice(system),                                  # system
            random.choice(language),                                # language
            fake.province()+fake.city(),                            # area
            random.choice(domain),                                  # referer_domain
            random.choice(path),                                    # referer_path
            random.choice(url)                                      # access_url
        ))
        j = j + 1
    sql = sql[:-1] + ';'
    cur.executemany(sql, data)
    print('{} inserted!'.format((i + 1) * j) + '\t' + datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    i = i + 1

conn.commit()
print('Table inserted successfully!')
conn.close()
from faker import Faker
import datetime


class CSVData:
    def __init__(self):
        self.fake = Faker(locale='zh_CN')

    def fake_data(self):
        col1 = self.fake.name()          # 随机生成一个姓名   '张三'
        col2 = self.fake.city()          # 城市名称         '辛集县'
        col3 = self.fake.street_name()   # 街道名称         '荆街'
        col4 = self.fake.country_code()  # 国家编号         'DM'
        col5 = self.fake.longitude()     # 经度            Decimal('134.520688')
        col6 = self.fake.iban()          # 银行账户         'GB39SNOA2073712937476'
        col7 = self.fake.catch_phrase()  # 公司            'Persistent bandwidth-monitored system engine'
        col8 = self.fake.hex_color()            # 颜色 16 进制编号   '#81b632'
        col9 = self.fake.iso8601(tzinfo=None)        # 以iso8601标准输出的日期   '1973-11-16T22:58:37'
        col10 = self.fake.time(pattern="%H:%M:%S")   # 时间（可自定义格式）    '11:21:52'

        col11 = self.fake.file_name(category=None, extension=None)   # 文件名   '看到.flac'
        col12 = self.fake.unix_device(prefix=None)   # unix设备    '/dev/vdu'

        col13 = self.fake.ipv4(network=False)        # ipv4地址  '104.225.105.10'
        col14 = self.fake.ipv6(network=False)        # ipv6地址  'dea6:ca11:39d0:b49f:fff1:82f1:bf88:698b'
        col15 = self.fake.uri()                      # url      'https://www.wei.com/terms/'
        col16 = self.fake.image_url(width=None, height=None)  # 图片url    'https://www.lorempixel.com/700/990'
        col17 = self.fake.user_agent()               # UA       'Opera/8.33.(Windows NT 5.1; an-ES) Presto/2.9.171 Version/10.00'
        col18 = self.fake.mac_address()              # MAC地址   'd6:38:cc:2a:76:b2'
        col19 = self.fake.safe_email()               # 安全邮箱   'mingli@example.net'

        col20 = self.fake.phone_number()             # 手机号   '18666613199'
        col21 = self.fake.ssn(min_age=18, max_age=90)            # 身份证号码  '460201193310128795'

        col22 = self.fake.profile(fields=None, sex=None)         # profile人物属性{'residence': '广东省呼和浩特县锡山龙街N座 403716', 'sex': 'M', 'website': ['http://zheng.org/'], 'birthdate': '1971-02-20', 'ssn': '513226197904080189', 'mail': 'jing95@hotmail.com', 'job': 'Ceramics designer', 'current_location': (Decimal('-86.424001'), Decimal('-153.969207')), 'blood_group': '0+', 'address': '广东省北京市永川深圳街w座 974761', 'company': '双敏电子传媒有限公司', 'username': 'xiajiang', 'name': '韩玉华'}
        col23 = self.fake.paragraphs(nb=3, ext_word_list=None)   # lorem  ['当然分析选择得到感觉关于.', '位置之间应用这种能够.', '你的处理上海.人员下载主要来自只是首页.图片有些所有详细发布.']

        line = '\"{0}\", \"{1}\", \"{2}\", \"{3}\", {4}, \"{5}\", \"{6}\" , \"{7}\" , \"{8}\" , \"{9}\" , \"{10}\" , \"{11}\" , \"{12}\" , \"{13}\" , \"{14}\" , \"{15}\" , \"{16}\" , \"{17}\" , \"{18}\" , \"{19}\" , \"{20}\" , \"{21}\" , \"{22}\"\n'.format(
                col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18, col19, col20, col21, col22, col23)
        # print(line)
        return line


def write_csv(filename):
    fh = open(filename, mode='w', encoding='utf-8')
    data = CSVData()
    for i in range(1000):
        line = data.fake_data()
        # fh.writelines(line)
        print('写入文件成功 ===:', i+1)
    fh.close()


def main():
    # 程序执行时间：
    start = datetime.datetime.now()

    file = r'E:\\CSV\\new_dbg.csv'
    write_csv(file)

    end = datetime.datetime.now()
    print(end - start)

if __name__ == "__main__":
    main()


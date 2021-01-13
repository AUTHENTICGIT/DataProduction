from mimesis import Person, Address, Code, Business, Text, Datetime, File, Path, Internet, Structure
from datetime import datetime


class CSVData:
    def __init__(self):
        self.person = Person(locale='zh')
        self.address = Address(locale='zh')
        self.code = Code()
        self.business = Business(locale='zh')
        self.text = Text(locale='zh')
        self.datetime = Datetime(locale='zh')
        self.file = File()
        self.path = Path()
        self.internet = Internet()
        self.structure = Structure()

    def mime_data(self):
        # col1 = self.person.full_name()
        col1 = self.person.last_name() + self.person.first_name()
        col2 = self.address.city()
        col3 = self.address.street_name()
        col4 = self.address.calling_code()
        col5 = self.address.longitude()
        col6 = self.code.imei()
        col7 = self.business.company()
        col8 = self.text.hex_color()
        col9 = self.datetime.formatted_datetime()
        col10 = self.datetime.time()

        col11 = self.file.file_name()
        col12 = self.path.dev_dir()
        col13 = self.internet.ip_v4()
        col14 = self.internet.ip_v6()
        col15 = self.internet.home_page()
        col16 = self.internet.stock_image()
        col17 = self.internet.user_agent()
        col18 = self.internet.mac_address()
        col19 = self.person.email()
        col20 = self.person.telephone()

        col21 = self.code.issn()
        col22 = self.person.social_media_profile()
        col23 = self.structure.html()

        line = '\"{0}\", \"{1}\", \"{2}\", \"{3}\", {4}, \"{5}\", \"{6}\" , \"{7}\" , \"{8}\" , \"{9}\" , \"{10}\" , \"{11}\" , \"{12}\" , \"{13}\" , \"{14}\" , \"{15}\" , \"{16}\" , \"{17}\" , \"{18}\" , \"{19}\" , \"{20}\" , \"{21}\" , \"{22}\"\n'.format(
                col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18, col19, col20, col21, col22, col23)

        # line = "mime data"
        # print(line)
        return line


def write_csv(filename):
    fh = open(filename, mode='w', encoding='utf-8')
    data = CSVData()
    for i in range(100):
        line = data.mime_data()
        fh.writelines(line)
        print('写入文件成功 ===:', i+1)
    fh.close()


def main():
    # 程序执行时间：
    start = datetime.now()

    file = r'E:\\CSV\\new_mime.csv'
    write_csv(file)

    end = datetime.now()
    print(end - start)


if __name__ == "__main__":
    main()

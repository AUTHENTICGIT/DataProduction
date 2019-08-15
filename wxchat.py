import itchat
import time

def lc():
    print('------Finish Login!----')
def ec():
    print('---------Exit!---------')

def Message(user, number):
    count = 0
    f = open('tmp/红楼梦.txt', encoding='utf-8')
    lines = f.readlines()
    if number == 'all':
        number = len(lines)
    for line in lines:
        data = line.strip()
        # 跳过空白行
        if len(data)!= 0 & count<number:
            print(line)
            itchat.send_msg(line, toUserName=user)
            count += 1
        elif count >= number:
            break
        if count%50 == 0:
            time.sleep(5)
    print('已发送{}条文本信息'.format(count))

def main():
    # 登陆微信
    itchat.auto_login(loginCallback=lc, exitCallback=ec)

    # 获取微信名
    users = itchat.search_friends(name='xly0583')
    userName = (users[0]['UserName'])

    # 发送全部条文本
    Message(userName, 70)
    # 发送图片
    itchat.send_image('tmp/Radar.png', toUserName=userName)

    time.sleep(1)
    itchat.logout()

if __name__ == '__main__':
    main()
from pymongo import MongoClient

# 1. 连接数据库
# 第一种方法：使用host和port IP连接
client = MongoClient(host='192.168.0.1', port=0000)
# 第二种方法：使用mongodb url
url = 'mongodb://host:port'
url = 'mongodb://username:password@host:port'   # 默认进入admin
url = 'mongodb://username:password@host/database_name'
client = MongoClient(url)

# 2. 增删查改
# 建立一个名为china的数据库
# china = client['china']
# 在user的基础上建立一个名为shandong的集合
# shandong = china['shandong']
# 也可以写成
collection = client['china']['shandong']

# 2.1 增：pymongo提供insert_one(),insert_many()两个方法来进行写操作
# 接受一个字典对象
collection.insert_one({'people_num':147000000})
# 接受一个字典列表
collection.insert_many([{'people_num':147000000}, {'city_num':16}])
collection.insert_one({'people_num':147000000, 'city_num':16, 'location':'east'})

# 2.2 查
collection.find_one()
collection.find_one({'people_num':147000000})
collection.find_one({'people_num':147000000, 'city_num':16})
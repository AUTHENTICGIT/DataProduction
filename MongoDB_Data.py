import pymongo
import os
from flask import json

# 向集合中插入多条记录
def insert_by_mongo(jsondata):
    conn = pymongo.MongoClient('localhost', 27017)
    # 获取数据库
    db = conn.testdb
    # 获取集合load_db():
    collection = db.clname
    try:
        collection.insert_many(jsondata)
        print('Success! Records +{}'.format(len(jsondata)))
    except Exception as e:
        print(e)
    conn.close()

# 向集合中插入一条记录
def insert_by_mongo_one(jsondata):
    conn = pymongo.MongoClient('localhost', 27017)
    # 获取数据库
    db = conn.testdb
    # 获取集合load_db():
    collection = db.clname
    # 向集合中插入一条记录
    try:
        collection.insert_one(jsondata)
        print('Success! Records +1!')
    except Exception as e:
        print(e)
    conn.close()

# 文件数据源，单个json
def load_data_file(path):
    fh = open(path, encoding='utf-8')
    count = 0
    jsonlist = []
    for line in fh:
        try:
            line = eval(line.rstrip())
            count = count + 1
            jsonlist.append(line)
            # print(count, type(line), line)
            # if(count == 10):
            #     break
        except Exception as e:
            print('[Ignore][insert exception]: line -', count, e)
            pass
        continue
    print(len(jsonlist))
    fh.close()
    return jsonlist

# 目录数据源，单个json，return [{},{},...,{}]
def load_data_filelist(filelist):
    jsonlist = []
    for file in filelist:
        try:
            fh = open(file, encoding='utf-8')
            data = fh.read()
            jsondata = json.loads(data)
            newjson = json_txt(jsondata)    # 处理key中包含的'.'
            jsonlist.append(newjson)
            fh.close()
        except Exception as e:
            print(e)
        continue
    return jsonlist

#**************************************************************************************
# 工具函数：
# 1. loopFile()
# 2. json_txt()
#**************************************************************************************

# 递归目录，遍历目录下的json文件 return [Str,Str,...,Str]
def loopFile(rootdir):
    filelist = []
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.json'):  # 判断是否.json，文件名字符串结尾匹配
                filelist.append(root+'\\'+file)
        for dir in dirs:
            loopFile(dir)
    return filelist

# 遍历key，处理_替换.  return {}
def json_txt(dic_json):
    if isinstance(dic_json, dict):
        for key in dic_json:
            if '.' in key:
                newkey = key.replace('.', '_')
                dic_json[newkey] = dic_json.pop(key)
                json_txt(dic_json[newkey])
            else:
                json_txt(dic_json[key])
    return dic_json

def main():
    # path = 'I:\\Saved\\New3\\ES_Doc70m.json'
    # data = load_data_file(path)
    # insert_by_mongo(data)

    dir_path = 'C:\\Program Files (x86)\\Adobe\\Adobe Creative Cloud\\CCXProcess\\js\\node_modules\\pngjs\\coverage'
    json_filelist = loopFile(dir_path)
    jsondata = load_data_filelist(json_filelist)
    print(jsondata[0])
    # insert_by_mongo(jsondata)
    # insert_by_mongo_one(jsondata[0])

if __name__ == '__main__':
    main()
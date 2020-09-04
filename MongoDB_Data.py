import pymongo

def insert_by_mongo(data):
    conn = pymongo.MongoClient('localhost',27017)
    # 获取数据库
    db = conn.testdb
    # 获取集合load_db():
    collection = db.test3
    # 向集合中插入多条记录
    try:
        collection.insert_many(data)
    except Exception as e:
        print(e)
    conn.close()


def load_data(path):
    fh = open(path, encoding='utf-8')
    count = 0
    list=[]
    for line in fh:
        try:
            line = eval(line.rstrip())
            count = count + 1
            list.append(line)
            # print(count, type(line), line)
            # if(count == 10):
            #     break
        except Exception as e:
            print('[Ignore][insert exception]: line -', count, e)
            pass
        continue
    print(len(list))
    return list

def main():
    path = 'I:\\Saved\\New3\\ES_Doc70m.json'
    data = load_data(path)
    insert_by_mongo(data)

if __name__ == '__main__':
    main()
import random
import time

import MySQLdb


def add(table_name, ip):
    try:
        db = MySQLdb.connect('localhost', 'root', 'lt980727', 'proxy', charset='utf8')
    except MySQLdb.OperationalError:
        print("连接失败")
    # except UnboundLocalError:
    #     db = MySQLdb.connect('localhost', 'root', 'lt980727', 'proxy', charset='utf8')
    my_cursor = db.cursor()
    try:
        my_cursor.execute(f"insert {table_name}(proxy) values('{ip}')")
    except MySQLdb.IntegrityError:
        pass
        # print('已过滤存在的ip')
    try:
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
    return my_cursor


def dlt(table_name, ip):
    try:
        db = MySQLdb.connect('localhost', 'root', 'lt980727', 'proxy', charset='utf8')
    except MySQLdb.OperationalError:
        print("连接失败")
    my_cursor = db.cursor()
    try:
        my_cursor.execute(f"delete from {table_name} where proxy='{ip}'")
    except MySQLdb.IntegrityError:
        print('删除失败！')

    try:
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
    return my_cursor


def showList(table_name):
    plist = []
    try:
        db = MySQLdb.connect('localhost', 'root', 'lt980727', 'proxy', charset='utf8')
    except MySQLdb.OperationalError:
        print("连接失败")
    my_cursor = db.cursor()
    try:
        my_cursor.execute(f"select * from {table_name}")
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
    res = my_cursor.fetchall()
    if len(res) > 0:
        for row in res:
            if not row[0] is None:
                plist.append(row[0])
        return plist


def random_proxy():
    p_list = showList('successstore')
    proxy = random.choice(p_list)
    print('当前IP池数量:', len(p_list))
    return proxy


if __name__ == '__main__':
    while True:
        time.sleep(3)
        print(random_proxy())
import random
import time
import MySQLdb
from setting import config


def add(table_name, ip):
    db = openDB()
    my_cursor = db.cursor()
    # except UnboundLocalError:
    #     db = MySQLdb.connect('localhost', 'root', 'lt980727', 'proxy', charset='utf8')
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
    db = openDB()
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
    db = openDB()
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


def clear_table(table_name):
    db = openDB()
    my_cursor = db.cursor()
    try:
        my_cursor.execute(f"delete * from {table_name}")
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()


def random_proxy():
    p_list = showList('successstore')
    try:
        proxy = random.choice(p_list)
        print('当前IP池数量:', len(p_list))
    except:
        proxy = 0
    return proxy


def openDB():
    try:
        db = MySQLdb.connect(config['host'], config['user'], config['passwd'], config['db'], charset=config['charset'])
    except MySQLdb.OperationalError:
        print("连接失败")
    return db


if __name__ == '__main__':
    print('等待清空失败IP池>>>')
    clear_table('failstore')
    while True:
        time.sleep(3)
        ls = random_proxy()
        if not ls is None:
            print(random_proxy())
from DBUtils.PooledDB import PooledDB
import MySQLdb
import MySQLdb.cursors
from config import DB_CONFIG
DB_CONFIG = dict(
        host='192.168.19.1',
        port=3306,
        db='test',
        user='ubuntu',
        passwd='123456',
        charset='utf8'
)
class DO():
    pool = PooledDB(MySQLdb,5,**DB_CONFIG)

    @classmethod
    def query(cls,sql):
        db = cls.pool.connection()
        cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        db.close()
        return res

    @classmethod
    def exe(cls,sql):
        db = cls.pool.connection()
        cur = db.cursor()
        cur.execute(sql)
        affected = cur.rowcount
        db.commit()
        cur.close()
        db.close()
        print 'affected : %s'%(affected)
        return affected

    @classmethod
    def exemany(cls,sql,args):
        db = cls.pool.connection()
        cur = db.cursor()
        cur.executemany(sql,args)
        affected = cur.rowcount
        db.commit()
        cur.close()
        db.close()
        print 'affected : %s'%(affected)
        return affected
if __name__ == '__main__':
    process_list = DO.exe("SHOW PROCESSLIST;")
    for pl in process_list:
        print pl
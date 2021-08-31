# coding=utf-8
import os
from bsddb3 import db

class Bdb_utils:

    _bsddb = ...

    def __init__(self,filename = None):
        
        # 数据库对象，提供数据读写
        # DB(dbEnv=None, flags=0)
        self._bsddb = db.DB()

        if filename != None:
            self.openDB(filename)

    def openDB(self,filename):

        # open(filename, dbname=None, dbtype=DB_UNKNOWN, flags=0, mode=0660, txn=None)
        self._bsddb.open(filename, db.DB_RECNO, 0 | db.DB_CREATE)

        # 文档 https://docs.oracle.com/database/bdb181/html/api_reference/C/dbopen.html
        # flags 标识
        # flags = 0 # 读写
        # DB_AUTO_COMMIT    # within a transaction
        # DB_CREATE     # Create the database. 数据库不存在时创建用，存在会失败
        # DB_EXCL   # Return an error if the database already exists.
        # DB_MULTIVERSION    # Open the database with support for multiversion concurrency control.
        # DB_NOMMAP  # Do not map this database into process memory
        # DB_RDONLY  # Open the database for reading only.
        # DB_THREAD     # Cause the DB handle returned by DB->open() to be free-threaded; that is, concurrently usable by multiple threads in the address space
        # 其他  

        # DBTYPE
        # DB_BTREE, DB_HASH, DB_HEAP, DB_QUEUE, DB_RECNO, or DB_UNKNOWN

    def mkDir(self,homedir):
        if homedir != None and homedir != "." and not os.path.exists(homedir):
            os.makedirs(homedir)  # 创建目录

    def mkFile(self,fileName):
        if fileName != None and str(fileName).endswith(".db") and not os.path.exists(fileName):
            f = open(fileName, "x")  # 创建文件
            f.close()

    # put(key, data, txn=None, flags=0, dlen=- 1, doff=- 1)
    def put(self, key, value):
        self._bsddb.put(key, value)

    # get(key, default=None, txn=None, flags=0, dlen=- 1, doff=- 1)
    def get(self, key):
        return self._bsddb.get(key)

    # delete(key, txn=None, flags=0)
    def delete(self, key):
        self._bsddb.delete(key)

    # get_size(key, txn=None)
    def get_size(self,key):
        return self._bsddb.get_size(key, txn=None)

    # keys(txn=None) 返回所有key对象
    # items(txn=None) 返回所有对象(k-v)
    # values(txn=None) 返回所有value值对象
    # has_key(key, txn=None) 判断是否有key
    def get_keys(self):
        return self._bsddb.keys()

    # sync(flags=0) Flushes any cached information to disk 
    # def sync(self):
        # self._bsddb.sync(flags=0)

    # exists(key, txn=None, flags=0)
    def exists(self,key):
        return self._bsddb.exists(key)

    # truncate(txn=None, flags=0)  Empties the database
    def trunctate(self):
        self._bsddb.truncate(txn=None, flags=0)
        
    # 删除数据库
    # remove(filename, dbname=None, flags=0)
    def remove(self,filename):
       if os.path.exists(filename):
            bdb = db.DB()
            bdb.remove(filename)
            bdb.close()

    # 数据库重命名
    # rename(filename, dbname, newname, flags=0)

    # close(flags=0)
    def close(self):
        self._bsddb.close()


if __name__ == '__main__':
    
    fileName = "bdb_test.db"

    bdb =  Bdb_utils()

    try:
        # 删除对象
        bdb.remove(fileName)
        # 打开对象
        bdb.openDB(fileName)
        # 插入
        bdb.put(1,"11")
        bdb.put(2,"22")
        # 获取
        print(bdb.get(1))
        print(bdb.get(2))

        # 删除
        bdb.delete(1)

        print(bdb.get(1))
    except Exception as e:
            raise e

    # 删除
    bdb.close()



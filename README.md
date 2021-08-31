# crawler_python-BerkeleyDB_base
python 嵌入式数据库BerkeleyDB基础使用

# python3对接嵌入式数据库BerkeleyDB

## 工具

python3
BerkeleyDB -> pip install berkeleydb

windows下安装失败使用非官方编译版本
bsddb3-6.2.9-cp36-cp36m-win_amd64.whl 
		-> https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygraphviz下载对应python版本的文件编译包 
		-> 平台python3.6下安装使用版本 pip install bsddb3-6.2.9-cp36-cp36m-win_amd64.whl

文档1：https://docs.jcea.es/berkeleydb/latest/
文档2：http://pybsddb.sourceforge.net/bsddb3.html

## 基础

BerkeleyDB ：Oracle出品，个人使用免费，商用收费，介于关系数据库与内存数据库之间，是一个k-v数据库。
特点：稳定，大数据量支持，单个文件最高256G

### 1：链接并打开数据库

使用python

```python
# 导入包
from bsddb3 import db
# 创建数据库对象
bsddb = db.DB()
# 打开对象
bsddb.open("test.db", db.DB_RECNO, 0 | db.DB_CREATE)

```



### 2：基础CRUD
目前使用DB_HASH插入出错，正在找问题

插入
put(key, data, txn=None, flags=0, dlen=- 1, doff=- 1)

查询 
get(key, default=None, txn=None, flags=0, dlen=- 1, doff=- 1)

删除
delete(key, txn=None, flags=0)



3：github地址


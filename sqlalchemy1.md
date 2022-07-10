mysql 
+----+-----------+
| id | name      |
+----+-----------+
|  1 | Javy      |
|  2 | Nash      |
|  3 | Yanxue    |
|  4 | Wujing    |
|  5 | Thmos     |
+----+-----------+

ORM Python
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

[
    User(1, 'Javy'),
    User(2, 'Nash'),
    User(3, 'Yanxue'),
    User(4, 'Wujing'),
    User(5, 'Thmos')
]
SQLAlchemy 
$ sudo pip3 install sqlalchemy

$sudo service mysql start                              [20:43:29]
 * Starting MySQL database server mysqld                                 [ OK ] 
$ mysql -u root 
#database默认编码  latin1 character set=utf8;
mysql> show variables like 'char%database';
+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| character_set_database | latin1 |
+------------------------+--------+
1 row in set (0.00 sec)
#新建study 编码格式UTF—8
mysql> create database study character set=UTF8;
#查看编码是否正确
mysql> show create database study\G

#创建db.py 运行

$ sudo pip3 install mysqlclient 
$ python3 db.py 
#MYSQL端查看新建的两张表                 
mysql> USE study
Database changed
mysql> SHOW TABLES;
+-----------------+
| Tables_in_study |
+-----------------+
| course          |
| user            |
+-----------------+
2 rows in set (0.00 sec)

#添加数据

sudo pip3 install faker
sudo pip3 install ipython
#ipython

In [1]: from faker import Faker                                                 

In [2]: fake=Faker('zh-cn')                                                     

In [3]: fake.name()                                                             
Out[3]: '张淑英'

In [4]: fake.address()                                                          
Out[4]: '澳门特别行政区宁德市海陵何路v座 839991'




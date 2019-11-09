#coding=utf-8

'''操作数据库'''

import pymysql
'''
链接本地数据库
1、数据库连接对象connection
host  字符串，MySQL的服务器地址
port  数字，MySQL的服务器端口号
user  字符串，用户名
passwd  字符串，密码
db  字符串，数据库名称
charset  字符串，连接编码

2、connection对象支持的方法
cursor()使用该连接创建并返回游标
commit()提交当前事务
rollback()回滚当前事务
close()关闭连接

使用cursor()方法获取操作游标

3、数据库的游标对象cursor
execute()：执行SQL、将结果从数据库获取到客户端
fetchone(),返回一条，  fetch*()方法：移动rownumber，返回数据
fetchmany(3)，返回3条,从上一次结束的位置开始执行
fetchall()，返回剩下的

4、select查询数据，开始--创建connection--获取cursor--execute()方法执行---fetch*获取数据--关闭cursor--关闭connection
'''
conn = pymysql.connect(host = '10.10.4.223',port=6001,user='weblogic',passwd='weblogic@223',db='orcl',charset='utf8')

cursor=conn.cursor()

sql="select * from sicmain"
cursor.execute(sql)
print(cursor.rowcount)
rs = cursor.fetchone()
print(rs)
rs = cursor.fetchmany(3)
print(rs)
rs = cursor.fetchall()
#print(rs)
for row in rs:
    print(row)

cursor.close()

conn.close()





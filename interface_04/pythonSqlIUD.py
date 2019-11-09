#coding=utf-8
import pymysql
'''
1、创建connection
2、获取cursor()游标
3、使用cursor.execute()执行insert()/update()/delete()更新数据库
    --异常？
        --否，conn.commit()提交事务
        --是，conn.rollback()回滚事务
4、关闭cursor，关闭释放资源
5、关闭conn

事务：访问和更新数据库的一个程序执行单元
'''
conn = pymysql.connect(host = '10.10.4.223',port=6001,user='weblogic',passwd='weblogic@223',db='orcl',charset='utf8')

cursor=conn.cursor()
sql_insert = "insert into siturnpolicy(auditno,comcode) values('A2019430461027','43040000')"
sql_update = "update siturnpolicy set comcode='43040000' where auditno='A2019430461027'"
sql_delete = "delete from siturnpolicy where auditno='A2019430461027'"

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)#对数据库产生了几行的影响
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

cursor.close()
conn.close()
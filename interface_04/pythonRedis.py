#coding=utf-8
#Python操作redis练习
import redis
'''

'''
r = redis.StrictRedis(host = '10.10.4.223',port=6001,user='weblogic',passwd='weblogic@223',db='orcl',charset='utf8')
rs = r.set('user2','Amy')
rs = r.get('user2')
d = {
    'user3':'li',
    'user4':'ming'
}
rs = r.mset(d)
l=['user3','user4']
rs = r.mget(l)
rs = r.append('user5','liu')
rs = r.delete('user5')

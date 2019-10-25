#coding = utf-8
from common import configHttp
from common import readExcell
url = r'E:\training\code\vip3test\interface_03\project\testData\data.xls'
#读取数据
xls_values = readExcell.Excel.read_excell(url)
print(xls_values)
#处理请求
#xls_value = ['https://www.wanandroid.com/user/login', 'login', 'post', "{'username':'liangchao','password':'123456'}", '0']
flags=[]
for xls_value in xls_values:
    case1 = configHttp.Request_h(xls_value[0],xls_value[3],xls_value[2])
    print(xls_value[0],xls_value[3],xls_value[2])
    r = case1.http_request()
    r_text = r.text
    print(r.text)
    try:
        flag = r.json()['errorCode']
    except:
        if r_text:
            flag=0
        else:
            flag=-1
    flags.append(flag)
print(flags)





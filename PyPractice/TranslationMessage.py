#coding = utf -8

import xml
import xml.etree.ElementTree as ET
import xml.dom.minidom
from  xml.dom import  minidom

filename = r'C:\Users\Administrator\Desktop\全单批改-主共保-收付费.xml'
doc = minidom.parse(filename).toxml('utf-8')
s = str(doc, encoding='utf-8')
# print(s)
res_lists = s.split('\n')
print(res_lists)
children1_dict = {
    'requesthead':'',
    'keyinfo':'',
    'bussdocinfo':'',
    'bussdealinfolist':'',
    'sumclauselist':'',
    'payeeplanlist':'',
}
requ_dict = {
    'request_type':'请求类型',
    'uuid':'',
    'sender':'',
    'server_version':'',
    'user':'',
    'password':'',
    'flowintime':''
}
key_dict = {
    'iscoinsVAT':'请求类型',
    'comcode':'',
    'documentno':'',
    'newdocumentno':'',
    'mergeflag':'',
    'ispaytiemsflag':'',
    'clausecludingmaping':''




}
for ele in res_lists:
    if 'request_type' in ele:
        # ele = list(ele)
        ele = ele + '请求类型'
        print(ele+'\n')
        continue
    else:
        print(ele+'\n')




with open('res.txt','a') as f:
    f.write(s)


















#xml.etree.ElementTree
# '''
# file_name = r'C:\Users\Administrator\Desktop\全单批改-主共保-收付费.xml'
# out_path = r'C:\Users\Administrator\Desktop\res.xml'
# tree = ET.parse(file_name)
# root = tree.getroot()
# children_nodes2 = root.getchildren()
# print(children_nodes2)
# print(type(children_nodes2))
# res_list = []
# for node in children_nodes2:
#     if node.tag == 'requesthead':
#         children_nodes3 = node.getchildren()
#         for node in children_nodes3:
#             print(node.tag)
#             if 'uuid' in node.tag:
#                 tag_name = '请求标识'
#                 node.attrib = tag_name
#                 l = [node.tag,node.text,node.attrib]
#                 res_list.append(l)
#                 print(res_list)
# '''



import re
import json
string1=input()
type1=string1[0]
num=re.search('\d\d\d+',string1)
name=re.search('!(.*?),',string1)
name=re.sub('!','',name.group())
name=re.sub(',','',name)
dic={}
dic['姓名']=name
dic['手机']=num.group()
#print(dic)
string2=re.sub('(.*?),','',string1)
string2=re.sub('\.','',string2)
string2=re.sub('(\d\d\d\d\d\d+)','',string2)
#print(string2)
listdata=['北京','天津','上海','重庆']
result=[]
if(string2[0:2] in listdata):
    result.append(string2[0:2])
    result.append(string2[0:2]+'市')
else:
    sheng=re.match('.*省',string2)
    if sheng == None:
        result.append('')
    else:
        result.append(sheng.group())
        string2=re.sub('.*省','',string2)
    
    shi=re.match('.*市',string2)
    if shi == None:
        result.append('')
    else:
        result.append(shi.group())
        string2=re.sub('.*市','',string2)

xian=re.match('.*[区|县|市]',string2)
if xian == None:
    result.append('')
else:
    result.append(xian.group())
    string2=re.sub('.*[区|县|市]','',string2)
    
zhen=re.match('.*[街道|镇|乡]',string2)
if zhen == None:
    result.append('')
else:
    result.append(zhen.group())
    string2=re.sub('.*[街道|镇|乡]','',string2)

if type1 == '2' or type1 == '3':
    lu=re.match('.*路',string2)
    if lu == None:
        result.append('')
    else:
        result.append(lu.group())
        string2=re.sub('.*路','',string2)
       
    hao=re.match('.*号',string2)
    if hao == None:
        result.append('')
    else:
        result.append(hao.group())
        string2=re.sub('.*号','',string2)

result.append(string2)
dic['地址']=result
json1=json.dumps(dic)
print(json1)
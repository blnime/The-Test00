'''
value = input("请入你需要的值:")
print("你输入的值 是",value)
'''

'''
print(len("wei,zaima"))
s
#题目：获取输入值的长度

num = input("请输入任意内容：")
print("输入内容的长度为：",len(num))
'''

#元组：内容固定，不可修改
#这是变量    这才是元组
stuple   =  (1,"hello",1.2,True,"555",555,32,23)

#下标
print(stuple[3])

#统计数量
num = stuple.count(555)
print(num)

#查找下标
nam = stuple.index(32)
print(nam)

#打印区间(左闭右开)
print(stuple[0:4])

print(stuple[-2])

#数组的操作
slist = [111,222,333,"张江",stuple,"我爱你","小恐龙",5.555]
print(slist[-2])

slist.append("222")
print(slist)

print(slist.count("222"))
print(slist.index("222"))

slist.insert(5,56789)
print(slist)

rr = slist.pop(6)
print(rr)
print(slist)

aa = slist.pop(slist.index("222"))
slist.insert(0,aa)
print(slist)

slist.extend("134567890")
print(slist)

slist.remove(222)
print(slist)

#字典的操作——按照键值对的方式来使用{"key":"value"}
sdict = {
    "name":"lsf",
    "high":"161",
    "sex":"woman"
    }
print(sdict)
print(sdict["name"])

#重新定义值，直接写
sdict["name1"] = "lili"
print(sdict)

bb = sdict.get("aa")
print(bb)

cc = sdict.pop("name1")
print(cc)
print(sdict)

print("----------------------------------------------------")
#二维操作
alist = [stuple,slist,sdict,"123",123,456,789]
dd = alist[1][3]
print(dd)
print(alist)


adict = {
    "11":"111",
    "22":"222",
    "33":{"1":"111",
            "2":"2222",
            "3":"3333"
    }
}
ee = adict["33"]["1"]
print(ee)
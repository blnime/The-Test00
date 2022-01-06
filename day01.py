from typing import NewType


print("hello,world")
print("123"*100)
print(123*100)
print(2>3)

"""
变量

赋值

"""
# aaa = input("请输入你想输入的值：")
# print("这是你输入的值：",aaa)

# bbb = input("请输入你要输入的第二个值：")
# print("这是为了说明input格式其实是字符串的输出：",aaa+bbb)

# aaa =float( input("请输入你想输入的值："))
# print("这是你输入的值的类型：",type(aaa))

# bbb = float(input("请输入你要输入的第二个值："))
# print("这是为了说明float的作用：",aaa+bbb)

#练习：获取两端输入值的长度，并计算长度和

eee = input("请输入第一段字符值：")

fff = input("请输入第二段字符值：")

print("第一段值的长度为",len(eee))
print("第二段值的长度为",len(fff))

print("第一段和第二段长度和为：",len(eee)+len(fff))
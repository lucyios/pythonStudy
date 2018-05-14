# a = [12,34,45,657,123,12,4,5,21,1,1,123]
#
# print(a.count(1),a.count(4325),a.count('x'))
#
#
# a.append(567)
#
# print(a)
#
#
#
# a.remove(1)
#
# print(a)
#
#
# a.reverse()#倒序排列数组内部元素
#
# print(a)
#
# a.sort()
#
# print(a)
#

# 将列表当做 堆栈用
#
# stack = [3,4,5]
#
# stack.append(6)
#
# stack.append(7)
#
# print(stack)
#
#
# stack.pop()
#
# print(stack)
#
# stack.pop()
#
# print(stack)


# 将列表当做 队列使用,一般效率比较低,如果从头添加元素或者删除元素,其他的元素都得一个一个移动

#列表推导式

# vec = [2,4,6]
#
# vec = [3 * x for x in vec]
#
# print(vec)
#
# vec = [3 * x for x in vec if x > 10]
#
# print(vec)


#字典

infoDict = {'name':'liluxin',
            'number':3456,
            'age':46,
            'week':34}

# print(infoDict['name'])
#
# print(infoDict.keys())
#
# if ('name' in infoDict):
#     print('yes')
# else:
#     print('NO')
#
# for k,v in infoDict.items():
#     print(k,v)

userInfo= {'id':34,
           'nickName':'lucy',
           'color':'yellow'}

for q,s in zip(infoDict,userInfo):
        print(q,s)





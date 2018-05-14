#coding=utf-8

#定义 hello world


# def helloworld():
#     print('hello world')
#
#
# helloworld()
#


# def area(width,length):
#     return width * length
#
# def print_welcome(name):
#     print('welcome',name)
#
# print_welcome("lucy")
#
# print(area(10,30))


#变量的作用域

# a = 30
#
# def printNum():
#     a = 99
#     print("a = ",a)
#
# def printNumer2():
#     print("a = ",a)
#
# printNum()
#
# printNumer2()

# 函数的返回值,可以指定,也可以返回None
# def sum(a,b):
#     return a + b
#
# print("sum =",sum(3,5))
#
# def empty(a,b):
#     return
#
# print("空值=",empty(1,3))


#可变参数列表,其实就是参数是一个容器,可以是一个数组
def arithmetic_mean(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(arithmetic_mean(23,45,23,546))


print(arithmetic_mean(34,567))


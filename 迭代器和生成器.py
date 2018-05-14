
import sys

list = [1,2,3,4]
it = iter(list)


# print(next(it))
#
# print(next(it))
#
# print(next(it))


# 可以使用  for  遍历

# for x in it:
#     print(x,end=" ")


# 使用 next 函数

# while True:
#     try:
#         print(next(it))
#     except  StopIteration:
#         sys.exit()


# 使用 yield 斐波那契数列

def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if (counter > n):
            return
        yield a
        a,b = b, a + b
        counter += 1

f = fibonacci(10)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
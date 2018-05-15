s = 'hello, world'
print(str(s))

print(repr(s))

print(1/3)

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    print(repr(x*x*x).rjust(4))


#str.format使用
print('We are the {} who say "{}!"'.format('tpson','Holle'))

print('{0} and {1}'.format('tposn','hundson'))

print('Hello,My name is {name},I am {age}'.format(name='liluxin',age=19))

table = {'Sjoerd':1234,'Jack':3245,'lucy':234}

print()

for name,phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name,phone))


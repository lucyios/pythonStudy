# class MyClass:
#
#
#     # def __init__(self):
#
#
#     i = 100
#     def myFunction(self):
#         return 'hello world'
#
# x = MyClass()
#
# print("my Class 中的属性i为:",x.i)
#
# print("当前类的调用方法:",x.myFunction())

class People:
    #定义基本属性
    name = ' '
    age = 0
    #定义私有属性,_开头
    _weight= 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self._weight = w
    def speak(self):
        print("%s 说:我 %d 岁." %(self.name,self.age))


person = People('liluxin',10,20)
person.speak()


class Person(People):
    grade  =''
    def __init__(self,n,a,w,g):
        People.__init__(self,n,a,w)
        self.grade = g
    def speak(self):
        print("%s 说:我 %d 岁了,我在读 %d 年级" %(self.name,self.age,self.grade))

studnet = Person('lucy',10,30,6)

studnet.speak()


class Speaker():
    topic = ' '
    name = ' '
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("I am %s, I an a speaker, 我演讲的主题是:%s" %(self.name,self.topic))

#多重继承

class Sample(Speaker,Person):
    a = ''
    def __init__(self,n,a,w,g,t):
        Person.__init__(self,n,a,w,g)
        Speaker.__init__(self,n,t)

test = Sample("Tim",23,34,1,"python")
test.speak()


class Parent:
    def myMethod(self):
        print("我是father")

class Son(Parent):
    def myMethod(self):
        print("我是son")

son = Son()
son.myMethod()

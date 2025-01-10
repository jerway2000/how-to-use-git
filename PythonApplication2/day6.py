#coding = utf-8
# 1、练习封装案例
# 2、练习私有属性和私有方法
# 3、练习单继承，多重继承案例
# 4、实现单例模式
"""
5、通过try进行异常捕捉，确保输入的内容一定是一个整型数，
然后判断该整型数是否是对称数，12321就是对称数，
123321也是对称数，否则就打印不是，非整型抛异常，不是对称数抛异常
"""

# 1、练习封装案例
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
        print("我叫%s,今年%d岁"%(self.name,self.age))
    def __str__(self):
        return "我叫%s,今年%d岁"%(self.name,self.age)

p = Person("张三",18)
p.say()
print(p)
# 2、练习私有属性和私有方法

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def __say(self):
        print("我叫%s,今年%d岁"%(self.__name,self.__age))
    def say(self):
        self.__say()

s = Person("张三",18)
s.say()
# 3、练习单继承，多重继承案例
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score = score
    def say(self):
        super().say()
        print("我的分数是%d"%self.score)

s = Student("张三",18,100)
s.say()

class Parent:
    def __init__(self,parent_name):
        self.parent_name = parent_name
class Son1(Parent):
    def __init__(self,son1_name , *args):
        self.son1_name= son1_name
        super().__init__(*args)
class Son2(Parent):
    def __init__(self,son2_name,*args ):
        self.son2_name = son2_name
        super().__init__(*args)
class Grandson(Son1,Son2):
    def __init__(self,grandson_name, *args):
        self.grandson_name = grandson_name
        super().__init__(*args)

g = Grandson("张三","张三爸爸","张三妈妈","张三祖父母")
print(g.grandson_name)
print(g.son1_name)
print(g.son2_name)
print(g.parent_name)
# 4、实现单例模式
class Singleton:
    __instance = None
    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)

# 5、通过try进行异常捕捉，确保输入的内容一定是一个整型数，
# 然后判断该整型数是否是对称数，12321就是对称数，
# 123321也是对称数，否则就打印不是，非整型抛异常，不是对称数抛异常
def is_symmetry(n):
    if str(n) == str(n)[::-1]:
        print("是对称数")
    else:
        print("不是对称数")
try:
    var= int(input("请输入一个整型数："))
    is_symmetry(var)
except Exception as e:
    print(e)




# 函数缺省参数练习
def printinfo(name, age=35, gender='male'):
    print("Name: ", name)
    print("Age ", age)
    print("Gender",gender)
    return


printinfo(age=50, name="miki")
printinfo(name="miki")
printinfo(name="xqc",gender='female')

def demo(num, *args, **kwargs):
    print("demo",num)
    print("demo",args)
    print("demo",kwargs)
    return
def demo2(num, *args, **kwargs):
    print("demo2",num)
    print("demo2",args)
    print("demo2",kwargs)
    demo(*args, **kwargs)
    return


demo(1,2,(3,4),[5,6,7], a=1,b=2,c=3)
demo2(1,2,(3,4),[5,6,7], a=1,b=2,c=3)
# 递归函数练习
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def fab(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

print(factorial(5))
# 元组、字典拆包练习
a,b,c=1,2,3
print(a,b,c)
a,b,c=[1,2,3]
print(a,b,c)
a,b,c=(1,2,3)
print(a,b,c)
a,b,c={'a':1,'b':2,'c':3}
print(a,b,c)
a,b,c={'a':1,'b':2,'c':3}.values()
print(a,b,c)
a,b,c={'a':1,'b':2,'c':3}.items()
print(a,b,c)
a,b,c={'a':1,'b':2,'c':3}.keys()
print(a,b,c)
a,b,c,*d=[1,2,3,4,5,6,7]
print(a,b,c,d)
a,b,c,*d=(1,2,3,4,5,6,7)
print(a,b,c,d)
a,b,c,*d={1,2,3,4,5,6,7}
print(a,b,c,d)
a,b,c,*d={'a':1,'b':2,'c':3,'d':4}
print(a,b,c,d)
a,b,c,*d={'a':1,'b':2,'c':3,'d':4}.values()
print(a,b,c,d)
a,b,c,*d={'a':1,'b':2,'c':3,'d':4}.items()
print(a,b,c,d)
a,b,c,*d={'a':1,'b':2,'c':3,'d':4}.keys()
print(a,b,c,d)
"""
3.设计一个类，实例化1个对象，会实现下面两种行为
需求
•一只 黄颜色 的 狗狗 叫 大黄
•具有  汪汪叫 行为
•具有  摇尾巴 行为
"""
class Dog:
    def __init__(self, color, name):
        self.color = color
        self.name = name
    def bark(self):
        print("汪汪叫")
    def wag(self):
        print("摇尾巴")

dog = Dog("黄色", "大黄")
dog.bark()
dog.wag()

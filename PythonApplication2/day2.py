# coding=utf-8
def different_type():
    # 自己定义变量赋值不同的数据类型并打印，并使用type
    a = 1
    b = 1.1
    c = 'hello'
    d = True
    e = [1, 2, 3]
    f = (1, 2, 3)
    g = {'name': '张三', 'age': 18}
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))
    print(e, type(e))
    print(f, type(f))
    print(g, type(g))

def number_system_conversion(num):
    # 将整型转为不同进制，进行输出
    print(bin(num))
    print(oct(num))
    print(hex(num))

def odd_sum():
    # 计算1到100之间的奇数和
    sum = 0
    for i in range(1, 101):
        if i % 2 == 1:
            sum += i
    print(sum)

def nine_nine_multiplication_table():
    # 输出九九乘法表
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%d' % (j, i, i * j), end='\t')
        print()
def count_one_in_binary( num ):
    # 统计一个整数对应的二进制数的1的个数。输入一个整数（可正可负，负数就按64位去遍历即可）， 输出该整数的二进制包含1的个数（使用位运算)
    count = 0
    if num < 0:
        num = num & 0xffffffff
        while num:
            count += 1
            num = num & (num - 1)
    else:
        while num:
            count += num & 1
            num >>= 1
    return count

def main():
    different_type()
    number_system_conversion(10)
    odd_sum()
    nine_nine_multiplication_table()
    print(count_one_in_binary(10))
    print(count_one_in_binary(-10))

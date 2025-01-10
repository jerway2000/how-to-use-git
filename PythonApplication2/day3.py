# coding=utf-8
import day3module
def find_unique_num(nums):
    # 有7个整数，其中有3个数出现了两次，1个数出现了一次， 找出出现了一次的那个数
    num = 0
    for i in nums:
        num ^= i
    return num
def func1():
    '''
      一个简单的for循环，从1打印到20，横着打为1排
    '''
    for i in range(1, 21):
        print(i, end=' ')
    print()
def say_hello(n):
    '''
      打印hello n次
      :param n: 打印次数
    '''
    for i in range(n):
        print('hello')
def find_two_unique_num(nums):
    # 有8个整数，其中有3个数出现了两次，2个数出现了一次， 找出出现了一次的那2个数
    num = 0
    for i in nums:
        num ^= i
    # 经过上面的循环，num 的值是两个只出现一次的数的异或结果

    mask = 1
    # 找到 num 中第一个为 1 的位，这个位在两个只出现一次的数中是不同的
    while num & mask == 0:
        mask <<= 1

    num1 = num2 = 0
    # 根据 mask 将数组分成两组，每组包含一个只出现一次的数
    for i in nums:
        if i & mask:
            num1 ^= i
        else:
            num2 ^= i

    return num1, num2

if __name__ =='__main__':
    nums=[5,2,2,3,3,4,4]
    print(find_unique_num(nums))
    func1()
    say_hello(3)
    day3module.print1()
    day3module.print2()
    day3module.print3()
    nums = [5, 2, 2, 3, 3, 4, 4, 6]
    print(find_two_unique_num(nums))
    # 练习列表基本使用，排序，生成式等各种操作
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list1.append(200)
    print(list1)
    list1.insert(1, 400)
    print(list1)
    list1 += [1000, 2000]
    print(list1)
    list1.sort()
    print(list1)
    print(list1[::-1])
    list3 = [x for x in range(1, 20)]
    print(list3)
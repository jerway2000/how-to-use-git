def q2(l1, l2):
    """
    # 2、求两个有序数字列表的公共元素
    :param l1: 任意列表1
    :param l2: 任意列表2
    :return: 列表的交集列表3
    """

    return [x for x in l1 if x in l2]


def q3(l1):
    """
    # 3、给定一个n个整型元素的列表a，其中有一个元素出现次数超过n / 2，求这个元素
    :param l1: 给定数组
    :return: 出现次数超过n/2的元素
    """

    vote, candidate = 1, 0
    for i in range(len(l1)):
        if l1[i] == l1[candidate]:
            vote += 1
        elif vote == 1:
            candidate = i
        else:
            vote -= 1
    return l1[candidate]


# 4、列表、元组，字典的相同点，不同点有哪些，请罗列
'''
列表和字典是可变类型，元组是不可变类型
列表和元组可以通过下标访问，字典能通过键值访问
列表和字典在初始化后可以增删，而元组不能

'''


def q5(t1, s1):
    """
    # 5、将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表
    :param t1: 元组
    :param s1: 集合
    :return: 列表
    """

    s1.update(t1)
    return list(s1)


def q6(l1):
    """
    # 6、在列表 [1,2,3,4,5,6] 首尾分别添加整型元素 7 和 0。
    :param l1: 原列表
    :return: 新列表
    """
    l1.insert(0, 0)
    l1.append(7)
    return l1


def q7(l1):
    """
    # 7、反转列表 [0,1,2,3,4,5,6,7] 。
    :param l1: 原列表
    :return: 新列表
    """
    return l1[::-1]


def q8(l1):
    """
    # 8、反转列表 [0,1,2,3,4,5,6,7] 后给出中元素 5 的索引号。
    :param l1: 原列表
    :return: 索引号
    """
    return l1[::-1].index(5)


def q9(l1):
    """
    # 9、分别统计列表 [True,False,0,1,2] 中 True,False,0,1,2的元素个数，发现了什么？
    :param l1: 原列表
    :return: 字典
    """
    return {i: l1.count(i) for i in l1}


def q10(l1):
    """
    # 10、从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’。
    :param l1: 原列表
    :return: 新列表
    """
    return [i for i in l1 if i != 'x']


def q11(l1):
    """
    # 11、从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除索引号为4的元素。
    :param l1: 原列表
    :return: 新列表
    """
    l1.pop(4)
    return l1


def q12(l1, flag):
    """
    # 12、删除列表中索引号为奇数（或偶数）的元素。
    :param l1: 原列表
    :param flag: True为奇数，False为偶数
    :return: 新列表
    """
    return [l1[i] for i in range(len(l1)) if i % 2 == flag]


def q13(l1):
    """
    # 13、清空列表中的所有元素。
    :param l1: 原列表
    :return: 新列表
    """
    l1.clear()
    return l1


def q14(l1):
    """
    # 14、对列表 [3,0,8,5,7] 分别做升序和降序排列。
    :param l1: 原列表
    :return: 升序和降序列表
    """
    return sorted(l1), sorted(l1, reverse=True)


def q15(l1):
    """
    # 15、将列表 [3,0,8,5,7] 中大于 5 元素置为1，其余元素置为0。
    :param l1: 原列表
    :return: 新列表
    """
    return [1 if i > 5 else 0 for i in l1]


def q16(l1):
    """
    # 16、遍历列表 [‘x’,‘y’,‘z’]，打印每一个元素及其对应的索引号。
    :param l1: 原列表
    :return: None
    """
    for i in range(len(l1)):
        print(i, l1[i])


def q17(l1):
    """
    # 17、将列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 拆分为奇数组和偶数组两个列表。
    :param l1: 原列表
    :return: 奇数组和偶数组
    """
    return [i for i in l1 if i % 2 == 1], [i for i in l1 if i % 2 == 0]


def q18(l1):
    """
    # 18、分别根据每一行的首元素和尾元素大小对二维列表 [[6, 5], [3, 7], [2, 8]] 排序。相当于按6,3,2进行排序，除非第一个元素相等，按第二个元素排序。
    :param l1: 原列表
    :return: 新列表
    """
    return sorted(l1, key=lambda x: (x[0], x[1]))


def q19(l1, l2):
    """
    # 19、从列表 [1,4,7,2,5,8] 索引为3的位置开始，依次插入列表 [‘x’,‘y’,‘z’] 的所有元素。
    :param l1: 原列表
    :param l2: 插入列表
    :return: 新列表
    """
    l1[3:3] = l2
    return l1


def q20():
    """
    # 20、快速生成由 [5,50) 区间内的整数组成的列表。
    :return: 列表
    """
    return list(range(5, 50))


def q21():
    """
    # 21、若 a = [1,2,3]，令 b = a，执行 b[0] = 9， a[0]亦被改变。为何？如何避免？----讲了深COPY和浅COPY再做
    :return: None
    """
    a = [1, 2, 3]
    b = a
    b[0] = 9
    print(a)
    print(b)
    a = [1, 2, 3]
    b = a.copy()
    b[0] = 9
    print(a)
    print(b)


def q22(l1, l2):
    """
    # 22、将列表 [‘x’,‘y’,‘z’] 和 [1,2,3] 转成 [(‘x’,1),(‘y’,2),(‘z’,3)] 的形式。
    :param l1: 列表1
    :param l2: 列表2
    :return: 列表
    """
    return list(zip(l1, l2))


def q23(d1):
    """
    # 23、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的键。
    :param d1: 字典
    :return: 列表
    """
    return list(d1.keys())


def q24(d1):
    """
    # 24、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的值。
    :param d1: 字典
    :return: 列表
    """
    return list(d1.values())


def q25(d1):
    """
    # 25、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有键值对组成的元组。
    :param d1: 字典
    :return: 列表
    """
    return list(d1.items())


def q26(d1):
    """
    # 26、向字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中追加 ‘David’:19 键值对，更新Cecil的值为17。
    :param d1: 字典
    :return: 字典
    """
    d1['David'] = 19
    d1['Cecil'] = 17
    return d1


def q27(d1):
    """
    # 27、删除字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中的Beth键后，清空该字典。
    :param d1: 字典
    :return: 字典
    """
    d1.pop('Beth')
    d1.clear()
    return d1


def q28(d1):
    """
    # 28、判断 David 和 Alice 是否在字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中。
    :param d1: 字典
    :return: None
    """
    print('David' in d1)
    print('Alice' in d1)


def q29(d1):
    """
    # 29、遍历字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21}，打印键值对。
    :param d1: 字典
    :return: None
    """
    for k, v in d1.items():
        print(k, v)


def q30():
    """
    # 30、若 a = dict()，令 b = a，执行 b.update({‘x’:1})， a亦被改变。为何？如何避免？----讲了深COPY和浅COPY再做
    :return: None
    """
    a = dict()
    b = a
    b.update({'x': 1})
    print(a)
    print(b)
    a = dict()
    b = a.copy()
    b.update({'x': 1})
    print(a)
    print(b)


def q31(l1):
    """
    # 31、以列表 [‘A’,‘B’,‘C’,‘D’,‘E’,‘F’,‘G’,‘H’] 中的每一个元素为键，默认值都是0，创建一个字典。
    :param l1: 列表
    :return: 字典
    """
    return {i: 0 for i in l1}


def q32(l1, t1):
    """
    # 32、将二维结构 [[‘a’,1],[‘b’,2]] 和 ((‘x’,3),(‘y’,4)) 转成字典。
    :param l1: 列表
    :param t1: 元组
    :return: 字典
    """
    return dict(l1 + t1)


def q33(t1, t2):
    """
    # 33、将元组 (1,2) 和 (3,4) 合并成一个元组。
    :param t1: 元组1
    :param t2: 元组2
    :return: 元组
    """
    return t1 + t2


def q34(t1):
    """
    # 34、将空间坐标元组 (1,2,3) 的三个元素解包对应到变量 x,y,z。
    :param t1: 元组
    :return: None
    """
    x, y, z = t1
    print(x, y, z)


def q35(t1):
    """
    # 35、返回元组 (‘Alice’,‘Beth’,‘Cecil’) 中 ‘Cecil’ 元素的索引号。
    :param t1: 元组
    :return: 索引号
    """
    return t1.index('Cecil')


def q36(t1):
    """
    # 36、返回元组 (2,5,3,2,4) 中元素 2 的个数。
    :param t1: 元组
    :return: 个数
    """
    return t1.count(2)


def q37(t1):
    """
    # 37、判断 ‘Cecil’ 是否在元组 (‘Alice’,‘Beth’,‘Cecil’) 中。
    :param t1: 元组
    :return: None
    """
    print('Cecil' in t1)


def q38(t1):
    """
    # 38、返回在元组 (2,5,3,7) 索引号为2的位置插入元素 9 之后的新元组。
    :param t1: 元组
    :return: 新元组
    """
    return t1[:2] + (9,) + t1[2:]


def q39():
    """
    # 39、创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素。
    :return: 集合
    """
    s1 = set()
    s1.update({'x', 'y', 'z'})
    return s1


def q40(s1):
    """
    # 40、删除集合 {‘x’,‘y’,‘z’} 中的 ‘z’ 元素，增加元素 ‘w’，然后清空整个集合。
    :param s1: 集合
    :return: 集合
    """
    s1.remove('z')
    s1.add('w')
    s1.clear()
    return s1


def q41(s1, s2):
    """
    # 41、返回集合 {‘A’,‘D’,‘B’} 中未出现在集合 {‘D’,‘E’,‘C’} 中的元素（差集）。
    :param s1: 集合1
    :param s2: 集合2
    :return: 集合
    """
    return s1 - s2


def q42(s1, s2):
    """
    # 42、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的并集。
    :param s1: 集合1
    :param s2: 集合2
    :return: 集合
    """
    return s1 | s2


def q43(s1, s2):
    """
    # 43、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的交集。
    :param s1: 集合1
    :param s2: 集合2
    :return: 集合
    """
    return s1 & s2


def q44(s1, s2):
    """
    # 44、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 未重复的元素的集合。
    :param s1: 集合1
    :param s2: 集合2
    :return: 集合
    """
    return s1 ^ s2


def q45(s1, s2):
    """
    # 45、判断两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 是否有重复元素。
    :param s1: 集合1
    :param s2: 集合2
    :return: None
    """
    print(s1.isdisjoint(s2))


def q46(s1, s2):
    """
    # 46、判断集合 {‘A’,‘C’} 是否是集合 {‘D’,‘C’,‘E’,‘A’} 的子集。
    :param s1: 集合1
    :param s2: 集合2
    :return: None
    """
    print(s1.issubset(s2))


def q47(l1):
    """
    # 47、去除数组 [1,2,5,2,3,4,5,‘x’,4,‘x’] 中的重复元素。
    :param l1: 原列表
    :return: 新列表
    """
    return list(set(l1))


def q48(s1):
    """
    # 48、返回字符串 ‘abCdEfg’ 的全部大写、全部小写和大下写互换形式。
    :param s1: 字符串
    :return: 大写、小写、大下写互换形式
    """
    return s1.upper(), s1.lower(), s1.swapcase()


def q49(s1):
    """
    # 49、判断字符串 ‘abCdEfg’ 是否首字母大写，字母是否全部小写，字母是否全部大写。
    :param s1: 字符串
    :return: None
    """
    print(s1.istitle())
    print(s1.islower())
    print(s1.isupper())


def q50(s1):
    """
    # 50、返回字符串 ‘this is python’ 首字母大写及字符串内每个单词首字母大写形式。
    :param s1: 字符串
    :return: 首字母大写以及字符串内每个单词首字母大写形式
    """
    return s1.capitalize(), s1.title()


def q51(s1):
    """
    # 51、判断字符串 ‘this is python’ 是否以 ‘this’ 开头，又是否以 ‘python’ 结尾。
    :param s1: 字符串
    :return: None
    """
    print(s1.startswith('this'))
    print(s1.endswith('python'))


def q52(s1):
    """
    # 52、返回字符串 ‘this is python’ 中 ‘is’ 的出现次数。
    :param s1: 字符串
    :return: 次数
    """
    return s1.count('is')


def q53(s1):
    """
    # 53、返回字符串 ‘this is python’ 中 ‘is’ 首次出现和最后一次出现的位置。
    :param s1: 字符串
    :return: 位置
    """
    return s1.find('is'), s1.rfind('is')


def q54(s1):
    """
    # 54、将字符串 ‘this is python’ 切片成3个单词。
    :param s1: 字符串
    :return: 列表
    """
    return s1.split()


def q55(s1):
    """
    # 55、返回字符串 ‘blog.csdn.net/xufive/article/details/102946961’ 按路径分隔符切片的结果。
    :param s1: 字符串
    :return: 列表
    """
    return s1.split('/')


def q56(s1):
    """
    # 56、将字符串 ‘2.72, 5, 7, 3.14’ 以半角逗号切片后，再将各个元素转成浮点型或整形。
    :param s1: 字符串
    :return: 列表
    """
    return [float(i) if '.' in i else int(i) for i in s1.split(',')]


def q57(s1):
    """
    # 57、判断字符串 ‘adS12K56’ 是否完全为字母数字，是否全为数字，是否全为字母？
    :param s1: 字符串
    :return: None
    """
    print(s1.isalnum())
    print(s1.isdigit())
    print(s1.isalpha())


def q58(s1):
    """
    # 58、将字符串 ‘there is python’ 中的 ‘is’ 替换为 ‘are’。
    :param s1: 字符串
    :return: 新字符串
    """
    return s1.replace('is', 'are')


def q59(s1):
    """
    # 59、清除字符串 ‘\t python \n’ 左侧、右侧，以及左右两侧的空白字符。
    :param s1: 字符串
    :return: 新字符串
    """
    return s1.lstrip(), s1.rstrip(), s1.strip()


def q60(s1, s2, s3):
    """
    # 60、将三个全英文字符串（比如，‘ok’, ‘hello’, ‘thank you’）分行打印，实现左对齐、右对齐和居中对齐效果。
    :param s1: 字符串1
    :param s2: 字符串2
    :param s3: 字符串3
    :return: None
    """
    print('{:<10}\n{:>10}\n{:^10}'.format(s1, s2, s3))


def q61(s1, s2, s3):
    """
    # 61、将三个字符串 ‘15’, ‘127’, ‘65535’ 左侧补0成同样长度。
    :param s1: 字符串1
    :param s2: 字符串2
    :param s3: 字符串3
    :return: None
    """
    print(s1.zfill(len(s3)))
    print(s2.zfill(len(s3)))
    print(s3)


def q62(l1):
    """
    # 62、将列表 [‘a’,‘b’,‘c’] 中各个元素用’|'连接成一个字符串。
    :param l1: 列表
    :return: 字符串
    """
    return '|'.join(l1)


def q63(s1):
    """
    # 63、将字符串 ‘abc’ 相邻的两个字母之间加上半角逗号，生成新的字符串。
    :param s1: 字符串
    :return: 新字符串
    """
    return ','.join(s1)


def q64():
    """
    # 64、从键盘输入手机号码，输出形如 ‘Mobile: 186 6677 7788’ 的字符串。
    :return: None
    """
    str1=input()
    str2='Mobile: '+str1[:3]+' '+str1[3:7]+' '+str1[7:]
    print('Mobile:', str2)


def q65():
    """
    # 65、从键盘输入年月日时分秒，输出形如 ‘2019-05-01 12:00:00’ 的字符串。
    :return: None
    """
    year = input('请输入年份')
    month = input('请输入月份')
    day = input('请输入日期')
    hour = input('请输入小时')
    minute = input('请输入分钟')
    second = input('请输入秒')
    print(year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second)


def q66():
    """
    # 66、给定两个浮点数 3.1415926 和 2.7182818，格式化输出字符串 ‘pi = 3.1416, e = 2.7183’。
    :return: None
    """
    a = 3.1415926
    b = 2.7182818
    print('pi = {:.4f}, e = {:.4f}'.format(a, b))


def q67():
    """
    # 67、将 0.00774592 和 356800000 格式化输出为科学计数法字符串。
    :return: None
    """
    a = 0.00774592
    b = 356800000
    print('{:.2e}, {:.2e}'.format(a, b))


def q68(l1):
    """
    # 68、将列表 [0,1,2,3.14,‘x’,None,’’,list(),{5}] 中各个元素转为布尔型。
    :param l1: 列表
    :return: 列表
    """
    return [bool(i) for i in l1]


def q69(s1):
    """
    # 69、返回字符 ‘a’ 和 ‘A’ 的ASCII编码值。
    :param s1: 字符
    :return: ASCII编码值
    """
    return ord(s1), ord(s1.upper())


def q70():
    """
    # 70、返回ASCII编码值为 57 和 122 的字符。
    :return: 字符
    """
    return chr(57), chr(122)


def q71(l1):
    """
    # 71、将列表 [3,‘a’,5.2,4,{},9,[]] 中 大于3的整数或浮点数置为1，其余置为0。
    :param l1: 列表
    :return: 新列表
    """
    return [1 if (type(i) == int or type(i) == float) and i > 3 else 0 for i in l1]


def q72(l1):
    """
    # 72、将二维列表 [[1], [‘a’,‘b’], [2.3, 4.5, 6.7]] 转为 一维列表。
    :param l1: 二维列表
    :return: 一维列表
    """
    return [j for i in l1 for j in i]


def q73(l1, l2):
    """
    # 73、将等长的键列表和值列表转为字典。
    :param l1: 键列表
    :param l2: 值列表
    :return: 字典
    """
    return dict(zip(l1, l2))


def q74(l1):
    """
    # 74、数字列表求和。
    :param l1: 数字列表
    :return: 和
    """
    return sum(l1)


# coding=utf-8
# 1、练习深copy与浅copy

from audioop import add
import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象
b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝
print('a:', id(a)) 
print('a4:', id(a[4]))
print('b:', id(b))
print('b4:', id(b[4]))
print('c:', id(c))
print('c4:', id(c[4]))
print('d:', id(d))
print('d4:', id(d[4]))

# 2、练习匹配单个字符，多个字符，匹配分组的正则表达式案例
import re

# 匹配单个字符
# . 匹配任意字符
# \w 匹配字母数字下划线
# \W 匹配非字母数字下划线
# \d 匹配数字
# \D 匹配非数字
# \s 匹配空白字符
# \S 匹配非空白字符
# [] 匹配[]中的任意一个字符
# [^] 匹配非[]中的任意一个字符
# [a-z] 匹配a-z中的任意一个字符

result = re.match('.', 'a')
print(result.group())
result = re.match('\\w', 'abc')
print(result.group())
result = re.match('\\W', '@#%^')
print(result.group())
result = re.match('\\d', '123')
print(result.group())
result = re.match('\\D', 'abc')
print(result.group())
result = re.match('\\s', ' ')
print(result.group())
result = re.match('\\S', '1')
print(result.group())
result = re.match('[a-z]', 'a')
print(result.group())
result = re.match('[^a-z]', '1')
print(result.group())
result = re.match('[a-z0-9]', '1')
print(result.group())

# 匹配多个字符
# * 匹配0个或多个字符
# + 匹配1个或多个字符
# ? 匹配0个或1个字符
# {n} 匹配n个字符
# {n,} 匹配n个以上字符
# {n,m} 匹配n-m个字符

result = re.match('[a-z]*', 'abc')
print(result.group())
result = re.match('[a-z]+', 'abc')
print(result.group())
result = re.match('[a-z]?', 'abc')
print(result.group())
result = re.match('[a-z]{3}', 'abc')
print(result.group())
result = re.match('[a-z]{3,}', 'abc')
print(result.group())
result = re.match('[a-z]{3,5}', 'abc')
print(result.group())
# 匹配开头结尾
# ^ 匹配开头
# $ 匹配结尾

result = re.match('^a', 'abc')
print(result.group())
result = re.match('.*c$', 'abc')
print(result.group())
# 邮箱匹配
result = re.match('\w+@\w+\.\w+','aslfkjalsf@asd.one')
print(result.group())
# 匹配1-99之间的数字
result = re.match('^[1-9][0-9]$|^[1-9]$','10')
print(result.group())
# 匹配分组
# () 括号内的内容为一个分组
# \num 引用分组num匹配到的内容
# (?P<name>) 给分组命名
# (?P=name) 引用分组name匹配到的内容
result = re.match('(\\d+)[a-z]\\1','123a123')
print(result.group())
result = re.match('(?P<name>\\d+)[a-z](?P=name)','123a123')
print(result.group())
# 匹配座机号
result = re.match('(\\d{3,4}-)?\\d{7,8}','010-12345678')
print(result.group())
# 3、练习search，findall,sub等案例
# search 匹配到一个就返回
result = re.search('\\d+','abc123abc123')
print(result.group())

def get_next_match(pattern, string):
    result = re.finditer(pattern, string)
    for i in result:
        yield i.group()

result_gen = get_next_match('\\d+','abc123abc123')
for i in result_gen:
    print(i)

# findall 匹配所有
result = re.findall('\\d+','abc123')
print(result)
# sub 替换
result = re.sub('\\d+','0','abc123')
print(result)
result = re.sub('\\d+',lambda x: str(int(x.group())*2),'abc123')
print(result)
# compile
string = 'time is 2019-01-01 14:24:31 现在是2019年1月1日 14时24分32秒'
pattern = re.compile(r'(\d{4}-\d{2}-\d{2}\s\d{2}\:\d{2}\:\d{2})[^\d]*(\d{4}年\d月\d日\s\d{2}时\d{2}分\d{2}秒)')
result = pattern.findall(string)
print(result)

# 4、练习正则表达式的贪婪与非贪婪模式
# 贪婪模式
result = re.match('.*b','abcabc')
print(result.group())
# 非贪婪模式
result = re.match('.*?b','abcabc')
print(result.group())

print(re.match('\w*','abc张三',re.A).group())

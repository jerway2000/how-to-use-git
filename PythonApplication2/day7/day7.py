from day7module1 import test
from day7module1 import test as test1
from wd_message import send_message, receive_message
import os
import sys
# 1.��ɰ���ʹ��
def test():
    print('module2 test()', __name__)

test1()
test()
send_message.send()
receive_message.receive()


# 3.���Ŀ¼��listdir��getcwd,chdir��ʹ��
def dir_operate():
    print(os.getcwd())
    os.chdir('day7')
    print(os.getcwd())
    print(os.listdir(os.getcwd()))

dir_operate()
# 2.����ļ����ı�ģʽ�Ķ���д
# 5.�����ͨ�ļ��ļ���seek���������ļ���seek
def file_operate():
    file1=open('TextFile1.txt','a')
    file1.write('helloworld')
    file1.close()
    file1=open('TextFile1.txt','r')
    file1.seek(5,os.SEEK_SET)
    print(file1.read(5))
    file1.close()

file_operate()

# 6.���Ŀ¼������ȱ���
def deep_search(path):
    for item in os.listdir(path):
        item_path=os.path.join(path,item)
        if os.path.isdir(item_path):
            deep_search(item_path)
        else:
            print(item_path)

deep_search(os.getcwd())

# 4.���python�Ĵ�����ϰ
if __name__ == '__main__':
    print(type(sys.argv))
    print(sys.argv)
# 7.eval()������ʹ��
    eval("__import__('os').system('dir')")
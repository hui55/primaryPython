if __name__ == '__main__':
    print 'think.py'

# 代码1
# def print_lyrics():
#     print "你好，我打印出来函数lyrics的内容"
#     print "Python非常有意思"
# def repeat_lyrics():
#     print_lyrics()

# repeat_lyrics()

# 代码2
# def sort_by(x, y):
#     if x>y:
#         return True
#     else:
#         return False


# print('对比结果: {0}'.format(sort_by(20,10)))

# 代码3
# samples = 'samplecode'
# print("打印字符串切片:{0}".format(samples[:]))

# 代码4
# families = ["chenhui","chenyanqiu","xuzhongxia"]
# for fam in families:
#     print fam

# print('chenhui in Famliy: {0}'.format('Chenhui' in families))

# for i in range(len(families)):
#     print 'Member{0}: {1} '.format(i,families[i])

# def nested_sum(raw_list):
#     total = 0
#     for rl in raw_list:
#         total += sum(rl)
#     return total

# test_sum_list = [[1,2],[3],[4,5,6]]
# print("计算总和: {0}".format(nested_sum(test_sum_list)))

# 代码5
# random = 'iamachinese'
# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else: 
#             d[c] += 1
#     return d
# print '打印统计数据: {0}'.format(histogram(random))

# def reverse_lookup(d,v):
#     print '告诉我字典的长度: {0}'.format(len(d))
#     results = []
#     for k in d:
#         if(d[k] == v):
#             results.append(k)
#     return results

# random_dict = {"a":"spring","b":"summer","c":"autumn","d":"winter"}
# print reverse_lookup(random_dict,"spring")

# 代码6
# 元组（是tuple不是元祖蛋糕谢谢。）

# def muti_divmod(a,b):
#     return divmod(a,b)
# print '元组返回值: {0}'.format(muti_divmod(7,3))

# def muti_args(*agrs):
#     print '入参: {0}'.format(agrs)
# muti_args('a','b')

# account, domain = 'chenhui2547@qianmi.com'.split("@")
# print '元组赋值，用户名:{0}, 域名:{1}'.format(account,domain)

# answers = ['a','b','c','d']
# for i,ele in enumerate(answers):
#     print '{0}:{1}'.format(i,ele)

# 代码7
# import os
# cwd = os.getcwd()
# print cwd

# import os
# def walk_cwd(dirname):
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname,name)
#         if os.path.isfile(path):
#             print path
#         else:
#             walk_cwd(path)

# walk_cwd(os.getcwd())

# try:
#     fin = open('random_file.txt')
# except:
#     print '没有找到文件错误'

# import os
# import hashlib
# file_hash = hashlib.md5()
# path  = os.getcwd() + '/README.md'
# print 'Print: {0}'.format(path)
# file_hash.update(open(path).read())
# print file_hash.hexdigest()

# 代码8
from student import Student
s = Student('chenhui',100)
s.print_score()
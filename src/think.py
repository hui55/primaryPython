if __name__ == '__main__':
    print '--- think.py ---'

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
# print的新用法，括号中说明多个变量用逗号分开
# families = ["chenhui","chenyanqiu","xuzhongxia"]
# for fam in families:
#     print fam

# print('chenhui in Famliy: {0}'.format('Chenhui' in families))

# for i in range(len(families)):
#     print 'Member_{0}: {1} '.format(i,families[i])

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
# from student import Student
# s = Student('chenhui',100)
# s.print_score()


## 代码9
# for a in [3,4.4,"life"]:
#     print '打印序列元素: {0}'.format(a)

## 代码10
# 总价100万的房子，全额贷款买房，前四年利率有折扣，分别是1%、2%、3%、3.5%
# 其余年份里房贷利率都是5%，逐年还款，每年最多偿还3万元。
# 问: 完全还清房贷需要多少年？

# year = 0
# total_amount = 500000.0
# interest_rates = (0.01,0.02,0.03,0.035)
# repay = 30000.0
# while total_amount > 0 :
#     year = year + 1
#     # print '第{0}年偿还贷款...'.format(year)
#     if year <= 4 :
#         interest = interest_rates[year-1]
#     else:
#         interest = 0.05
#     total_amount = total_amount * (interest + 1) - repay
#     print '剩余金额%.2f' % total_amount

# print '恭喜您，通过{0}年终于还清了房贷'.format(year)

## 代码11
## 函数定义: 形参
## 函数调用: 实参
# def print_hello():
#     """ print hello world """
#     print 'Hello World'
# help(print_hello)
# print_hello()
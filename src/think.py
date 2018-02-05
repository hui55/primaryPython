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
random = 'iamachinese'
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else: 
            d[c] += 1
    return d
print '打印统计数据: {0}'.format(histogram(random))
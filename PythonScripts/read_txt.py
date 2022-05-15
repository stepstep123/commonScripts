'''
open 函数
open函数读取内容
写入字典
'''


from collections import defaultdict

file = "../"
dic = defaultdict(int)
with open(file, 'r+' "encoding='utf-8") as f:
    for line in f.readlines():
        temp = line.split(",")
        dic[temp] += 1



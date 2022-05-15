
'''
给一个txt文件每行末尾添加一个字符，且不换行
1.先追加存入列表
2.从列表中读出，写入文件
'''

file1 = "./raw.txt"
file2 = "./src.txt"


def write():
    temp = []
    with open(file1, "r") as f:
        for line in f.readlines():
            line = line + line.replace('\n', " ") + str(0) #每行都有一个换行符号，注意替换掉
            temp.append(line)
    with open(file2, 'w') as f:
        for line in temp:
            f.writelines(line + '\n') #记得给每行添加一个换行符号
write()

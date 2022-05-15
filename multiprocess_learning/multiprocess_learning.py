#!/usr/bin/env/python
# coding=utf-8

'''
Description:
Author: yujianghua
Date: 2022-04-07 21:50:52
Email: paulyujh@163.com
'''

import multiprocessing
import time

def func(mylist, i):
    print("进入func")
    while True:
        print('main'*5)
        i += 1
        mylist.append(i)  # 子进程改变List,主进程跟着改变
        time.sleep(1)

def func1(mylist):
    print("进入func1")
    while True:
        print("1"*10)
        time.sleep(2)
        print(mylist)

if __name__ == "__main__":
    mylist = multiprocessing.Manager().list()  # 主进程与子进程共享这个List
    p = multiprocessing.Process(target=func, args=(mylist, 0,))
    p1 = multiprocessing.Process(target=func1, args=(mylist,))
    p.start() #启动进程p
    p1.start() #启动进程p1
    p.join() #等待进程p终止
    p1.join() #等待进程p1终止



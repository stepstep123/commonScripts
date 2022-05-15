#!/usr/bin/env/python
# coding=utf-8

'''
Description:
Author: yujianghua
Date: 2022-04-08 21:25:44
Email: paulyujh@163.com
'''

# encoding:utf-8
import threading
import time
import random


class sleepThread(threading.Thread):
    def __init__(self, alist):
        threading.Thread.__init__(self)
        print(self.name+ ' is created!')
        self.alist = alist

    def run(self):
        # randomTime = random.randint(1,9) # 生成 1~9的随机整数
        for i in range(10):
            self.alist.append(i)
            time.sleep(3)
        # print(self.name+ ' slept for '+str(3)+' seconds')


class sleepThread1(threading.Thread):
    def __init__(self, alist):
        threading.Thread.__init__(self)
        print(self.name+ ' is created!')
        self.alist = alist

    def run(self):
        # randomTime = random.randint(1,9) # 生成 1~9的随机整数
        for i in range(10):
            print(self.alist)
            time.sleep(5)
        # print(self.name+ ' slept for '+str(3)+' seconds')

if __name__ == '__main__':
    threads = []
    alist = []
    # for i in range(5):  # 创建5个进程
    th = sleepThread(alist)
    threads.append(th)
    th1 = sleepThread1(alist)
    threads.append(th1)
    th.start()
    while True:
        print(alist)
    # th1.start()

    # for t in threads:
    #     t.join()
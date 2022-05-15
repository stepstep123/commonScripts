#!/usr/bin/env/python
# coding=utf-8

'''
Description:
Author: yujianghua
Date: 2022-04-08 09:15:52
Email: paulyujh@163.com
'''
# coding:utf-8
#进程间的通信s
from multiprocessing import Process, Queue
import multiprocessing
import os, time, random

# 写数据进程执行的代码:
def write(q):
    for value in range(20):
        print('Put %s to queue...' % value)
        q.put(value)
        print(q)
        time.sleep(3)

# 读数据进程执行的代码:
def read(q):
    while True:
        time.sleep(5)
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = multiprocessing.Manager().list()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
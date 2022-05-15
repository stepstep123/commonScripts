#!/usr/bin/env/python
# coding=utf-8

'''
Description:
Author: yujianghua
Date: 2022-04-10 09:42:33
Email: paulyujh@163.com
'''

import threading
import time

def sleepThread1(threadName, alist):
	for i in range(10):
		alist.append(i)
		time.sleep(1)

def sleepThread2(threadName, alist):
	while True:
		print(alist)
		time.sleep(2)

if __name__ == '__main__':

	gloabList = [] #全局变量，用来线程通信

	th1 = threading.Thread(target=sleepThread1, args=('Thread1',gloabList))
	th2 = threading.Thread(target=sleepThread2, args=('Thread2', gloabList),)

	th1.start() #开启线程th1
	th2.start() #开启线程th2
	th1.join()  #等待线程th1结束
	th2.join()  #等待线程th2结束












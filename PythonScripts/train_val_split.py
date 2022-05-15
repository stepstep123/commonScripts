#!/usr/bin/env python
# encoding: utf-8

'''
说明：
将dataFrame数据划分为tran、test格式
'''

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('../banners/label_list.txt', sep=' ', header=None)
X, y = df[0].values, df[1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

for x, label in zip(X_test, y_test):
	print(x, label)
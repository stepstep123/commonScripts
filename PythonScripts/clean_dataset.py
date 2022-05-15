import os
import json
import sys
import subprocess
from tqdm import tqdm
from PIL import Image


'''
说明：
清除无效的RGB数据
'''

imgdir = sys.argv[1]
imglist = os.listdir(imgdir)
for img in tqdm(imglist):
    imgpath = os.path.join(imgdir, img)
    try:
        imgdata = Image.open(imgpath).convert('RGB')
    except:
        cmd = 'rm {}'.format(imgpath)
        print(cmd)
        #subprocess.call(cmd, shell=True)

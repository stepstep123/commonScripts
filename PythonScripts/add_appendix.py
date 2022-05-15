import sys
import os
import subprocess
from tqdm import tqdm


'''
说明
为文件添加后缀
'''
imgdir = sys.argv[1]

imglist = os.listdir(imgdir)

for img in tqdm(imglist):
    imgpath = os.path.join(imgdir, img)
    if not img.endswith('g'):
        cmd = 'mv {} {}'.format(imgpath, imgpath+'.jpg')
        subprocess.call(cmd, shell=True)

import os, random, shutil
 
'''
 说明：
 按照一定比例从文件夹a移动文件到b
'''
 
def moveFile(fileDir, tarDir):
    pathDir1 = os.listdir(fileDir)  # 取图片的原始路径
    
    i = 0 
    for rootPath in pathDir1:
        use = rootPath.split('_')[1]
        if use == 'normal':
            i+= 1
            path1 = os.path.join(fileDir, rootPath)
            pathDir = os.listdir(path1)  # 取图片的原始路径
            picknumber = 300  # 按照rate比例从文件夹中取一定数量图片
            sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
            print(sample)
            print(len(sample))
  
            for name in sample:
                print('src:', path1 +'/'+name)
                print('dst:',tarDir+ name)
                src = path1 +'/'+name
                dst = tarDir+ name
                # exit()
                shutil.copyfile(src,dst)
            # shutil.move(fileDir + name, tarDir + name)
    print('i:', i)
 
 
if __name__ == '__main__':
    fileDir = "/disk2/suaimin/dataset/terror/train"  # 源图片文件夹路径
    tarDir = '/disk2/yjh/datasets/badScene/qse_v3/others/'  # 移动到新的文件夹路径
    moveFile(fileDir, tarDir)
 
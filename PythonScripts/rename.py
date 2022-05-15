import os, random, shutil

'''
说明：
将文件从a复制到b
支持多层文件夹嵌套
'''

def renameCopyFile(fileDir, tarDir):
    pathDir1 = os.listdir(fileDir)  # 取图片的原始路径
    for logoItem in pathDir1:
        path2 = os.path.join(fileDir, logoItem)
        pathDir2 = os.listdir(path2)
        for rootPath in pathDir2:
            path1 = os.path.join(path2, rootPath)
            try:
                pathDir = os.listdir(path1)  # 取图片的原始路径
                try:
                    className = rootPath.split('_')[0]
                    for name in pathDir:
                        print('src:', path1 +'/'+name)
                        print('dst:',tarDir + className + '/' + rootPath + '_' + name)
                        src = path1 +'/'+ name
                        dst = tarDir + className + '/' + rootPath + '_' + name
                        shutil.copyfile(src,dst)

                except:
                    continue
            except:
                    continue

if __name__ == '__main__':
    fileDir = "/disk2/yujianghua/project/docker_ship/Yolov5_DeepSort_Pytorch_ship/yolov5/data/logo"  # 源图片文件夹路径
    tarDir = '/disk2/yjh/datasets/badScene/qse_v3/'  # 移动到新的文件夹路径
    renameCopyFile(fileDir, tarDir)
#!/usr/bin/python3

# 提取目录下所有图片,更改尺寸后保存到另一目录
# from PIL import Image
import os.path
import sys, os
import cv2

# 取中心图片
def crop_center(img,cropx,cropy):
    y,x,c = img.shape
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)    
    return img[starty:starty+cropy,startx:startx+cropx]


def convertjpg(inputdir, outdir, crop_size=224):

    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    files= os.listdir(inputdir) #得到文件夹下的所有文件名称
    sorted_files = sorted(files)
    for file in sorted_files:
        print(file)
        img = cv2.imread(inputdir + '/' + file)
        #cv2读取后的图片数据默认为bgr顺序排列
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        print(img.shape)
        weight = img.shape[0]
        height = img.shape[1]
        if weight < height:
            img = cv2.resize(img, (int(height/weight * 224), 224))
        else:
            img = cv2.resize(img, (224, int(weight/height * 224)))

        print(img.shape)
        img = crop_center(img,224,224)
        (w,h,c) = img.shape
        if w!= 224 or h!=224 or c!=3:
            print("error shape ", img.shape)
            sys.exit(-1)

        save_name = file.split(".")[0] + '.jpg'
        save_file = os.path.join(outdir, os.path.basename(save_name))
        cv2.imwrite(save_file, img)


def convertjpg2(inputdir, outdir, width=224, height=224):

    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    files= os.listdir(inputdir) #得到文件夹下的所有文件名称
    for file in files:
        try:
            print(file)
            img = cv2.imread(inputdir + '/' + file)
            img = cv2.resize(img, (width,height))
            save_name = file.split(".")[0] + '.jpg'
            save_file = os.path.join(outdir, os.path.basename(save_name))
            cv2.imwrite(save_file, img)
        except Exception as e:
            print(e)


if __name__ == "__main__":

    if len(sys.argv) !=3:
        print("Usage: ", sys.argv[0], " input_path  output_path")
        sys.exit(-1)

    convertjpg(sys.argv[1], sys.argv[2])

#!/usr/bin/python3

# 提取目录下所有图片,更改尺寸后保存到另一目录
# from PIL import Image
import os.path
import sys, os
import cv2

def convertjpg(inputdir, outdir, width=224, height=224):

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

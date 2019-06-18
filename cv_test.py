import cv2
import time


# 修改图片像素重新保存
def resize_img():
    
    size = 227

    img = cv2.imread("input/cat.jpg")
    cv2.imshow("img",img)

    img_resize = cv2.resize(img, (size, size), interpolation=cv2.INTER_CUBIC )
    cv2.imwrite('output/%d.jpg'%(size), img_resize)
    cv2.imshow("img_resize",img_resize)
    cv2.waitKey()


if __name__ == "__main__":
    resize_img()
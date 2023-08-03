import numpy as np

numpy=np.arange(15)
list1=list(range(15))

# print(numpy)
# print(list1)

# a=np.arange(5)
# b=np.arange(10,21,5)
# c=np.arange(0,1,.3)
# d=np.arange(30,10,-5)

# print(a,b,c,d)

# shape=numpy.reshape(3,5)
# print(shape)

# a=np.zeros((2,2,2))
# print(a)

# a=np.linspace(0,2,6)
# print(a)

# a=np.arange(5)
# a=a.astype("float64")
# print(a)
#  I ♥ NEW YORK

# a=[1,2,3,4]+[5,6,7,8]
# print(a)
# a=np.array([1,2,3,4])
# b=np.array([5,6,7,8])
# # print(a,b, a>ggb)

import cv2

# img=cv2.imread("cat.png")
# # print(img)
# cv2.imwrite("cat_copy.png", img)
# x=300
# y=300

# randoms=np.random.randint(0,255,(y*x*3),dtype=np.uint8)
# img=randoms.reshape(y,x,3)
# # cv2.imwrite("random.png",img)

# img[:100, :100]=(255,0,0)
# img[100:200, :100]=(0,255,0)
# img[200:300, :100]=(0,0,255)
# BGR

# cv2.imshow("test", img)
# cv2.waitKey()

import cv2
number=0

cam=cv2.VideoCapture(0)
while True: 
    suc, frame=cam.read()

        # frame[200:400, :200]=(255,0,0)
        # frame[200:400, 200:400]=(0,255,0)
        # frame[200:400, 400:600]=(0,0,255)

    cv2.imshow("test", frame)

    key=cv2.waitKey(1)
    if key==ord("1"):
        break
    if key==ord("2"):
        cv2.imwrite(f"cap/capture{number}.png", frame)
        number=number+1
cv2.waitKey()


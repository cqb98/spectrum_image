# -*- coding: utf-8 -*-  
from PIL import Image
import PIL.ImageOps  
import numpy as np
import matplotlib.pyplot as plt
import math
import struct
import sys

import FFT


imageName="test.jpg"
if(len(sys.argv)>1):
	imageName=sys.argv[1]

try:
	img = Image.open(imageName)
	
except:
	print(imageName," not exist!")
	exit(0)
 
# 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
img = img.convert('L')
img=PIL.ImageOps.invert(img)
img=img.transpose(Image.FLIP_TOP_BOTTOM)
img=np.array(img)

xscale=4
yscale=64
 

def limitS8(x):
	x=round(x)
	if( x > 127 ):
		return 127
	if( x < -128):
		return -128
	return int(x)

def line(data,xl):
	power=math.ceil(math.log2(xl))
	length=2**power;
	remain=length-xl
	left=remain//2
	right=remain-left
	#print("left,right",left,right)
	data= ([0+0j]*left) + data + ([0+0j]*right)
	#d=data
	d=data[length//2:]+data[0:length//2]
	return FFT.iFFT(d,power)
	
'''
# 自定义灰度界限，大于这个值为黑色，小于这个值为白色
threshold = 200
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
# 图片二值化
photo = Img.point(table, '1')
'''


xlen=img.shape[1]
ylen=img.shape[0]

length=2**math.ceil(math.log2(xlen*xscale))
print("FFT point:",length)
print("file size:",(2*length*ylen*yscale)// (1e3),"kb")

spectrums=[]
f=open("out.txt","wb")
for i in range(ylen):
	s=[]
	for j in range(xlen):
		val=img[i][j]/255#[y][x]

		#display type

		'''
		if(val!=0):
			val=5*math.log10(val/0.0032)
		'''
		if(val< (5/256)):
			val=0
		s+=([val]*xscale);


	#s=[10]*(xlen*xscale)
	d=line(s,xlen*xscale)
	#print(d)
	#spectrums.append(s);


	bin=b""
	for v in d:
		b= struct.pack("bb", limitS8(v.real) , limitS8(v.imag) ) 
		bin+=b
	f.write(yscale*bin)

f.close()

print("finish")
print("run command to use:")
print("hackrf_transfer -t out.txt -f 490e6 -s 4e6 -a 0 -x 32")
	

'''
plt.figure("pica")
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.show()
'''

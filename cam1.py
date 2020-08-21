import pygame
import os
import pygame.camera
from array import array
def normalize(snd_data):
	MAXIMUM=863000
	times=1
	p=[]
	q=[]
	#print(snd_data)
	p=snd_data.split('\n')
	for i in p:
		if i!='':
			j=int(i)
			q.append(j)
	ff=max(q)
	times=float(MAXIMUM)/ff
	print(times)
	r=''
	print("before r")
	c=0
	for i in range(0,100):
		r+=convert(int(q[i]*times))
	#print(r)	
	return r
def convert(num):
	print("num:"+str(num))
	a=''
	while(num!=0):
		if(num%2==1):
			a+='1'
		elif(num%2==0):
			a+='0'
		num=num/2
	print(a)
	return a
pygame.camera.init()
cam=pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
img=cam.get_image()
pygame.image.save(img,"live.jpg")
os.system('javac ImageTest.java')
os.system('java ImageTest')
f=open("imagejava.txt","r")
s = f.read()
y=normalize(s)
x=int(y)
#z=convert(x)
f=open("imageop.txt","a")
f.write(y)

import os
print("This is seed")
print("Calling cam.py")
os.system('python cam1.py')
print("Calling ping")
for i in range(0,8):
	os.system('python ping.py')
print("Calling rng.py")
os.system('python rng.py')
ff=open("final.txt","a");
fc=open("imageop.txt","r");
#ft=open("timeop.txt","r");
fp=open("pingop.txt","r");
fa=open("audioop.txt","r");
s='';
s+=fc.read()+fp.read()+fa.read()
ff.write(s);

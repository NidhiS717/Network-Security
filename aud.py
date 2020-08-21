from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave
import os

THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 44100
def normalize(snd_data):
	MAXIMUM=90000
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
def record():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    while num_silent<100:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)
        num_silent +=1

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()
    #r = normalize(r)
    return sample_width, r

def record_to_file(path):
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()

if __name__ == '__main__':
    #i = 0
    print("please speak a word into the microphone")
    record_to_file('aud.wav')
    print("done - result written to aud.wav")
    os.system('javac AudTest.java')
    os.system('java AudTest')
    f=open("audioop.txt","r")
    s = f.read()
    print("S: ",s)
    y=normalize(s)
    x=int(y)
    #z=convert(x)
    f=open("audioop2.txt","a")
    f.write(y)
		#i = i+1

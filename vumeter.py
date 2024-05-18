import alsaaudio as alsa
import time
import audioop
import math
import RPi.GPIO as GPIO
import time


def ON(pin):
	GPIO.output(pin,GPIO.HIGH)
	return

def OFF(pin):
	GPIO.output(pin,GPIO.LOW)
	return

def POWERGPIO(p29,p31,p33,p35,p37,p36,p38,p40):
	if(p29):
		ON(29)
	else:
		OFF(29)
	if(p31):
		ON(31)
	else:
		OFF(31)
	if(p33):
		ON(33)
	else:
		OFF(33)
	if(p55):
		ON(35)
	else:
		OFF(35)
	if(p37):
		ON(37)
	else:
		OFF(37)
	if(p36):
		ON(36)
	else:
		OFF(36)
	if(p38):
		ON(38)
	else:
		OFF(38)
	if(p40):
		ON(40)
	else:
		OFF(40)
	return

def SETGPIO(d):
	if(d == 'a'):
		POWERGPIO(0,0,0,0,0,0,0,0)
	elif(d == 'b'):
		POWERGPIO(1,0,0,0,0,0,0,0)
	elif(d == 'c'):
		POWERGPIO(1,1,0,0,0,0,0,0)
	elif(d == 'd'):
		POWERGPIO(1,1,1,0,0,0,0,0)
	elif(d == 'e'):
		POWERGPIO(1,1,1,1,0,0,0,0)
	elif(d == 'f'):
		POWERGPIO(1,1,1,1,1,0,0,0)
	elif(d == 'g'):
		POWERGPIO(1,1,1,1,1,1,0,0)
	elif(d == 'h'):
		POWERGPIO(1,1,1,1,1,1,1,0)
	elif(d == 'i'):
		POWERGPIO(1,1,1,1,1,1,1,1)
	return
print ("##############################")
print ("# Waiting for a song to play #")
print ("##############################")

inp = alsa.PCM(alsa.PCM_CAPTURE, alsa.PCM_NORMAL, 'hw:Loopback,1,0')
out = alsa.PCM(alsa.PCM_PLAYBACK, alsa.PCM_NORMAL, 'plughw:0,0')

inp.setchannels(2)
inp.setrate(44100)
inp.setformat(alsa.PCM_FORMAT_S16_LE)
inp.setperiodsize(320)

out.setchannels(2)
out.setrate(44100)
out.setformat(alsa.PCM_FORMAT_S16_LE)
out.setperiodsize(320)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

status = 1

lo = 10000
hi = 32000

log_lo = math.log(lo)
log_hi = math.log(hi)

while True:
	l,data = inp.read()
	if l:
		try:
			d = audioop.max(data, 2)
			vu = (math.log(float(max(audioop.max(data, 2),1)))-log_lo)/(log_hi-log_lo)
			teste = chr(ord('a')+min(max(int(vu*20),0),19))
			if teste != 'a':
				print (teste)
			if d>0:
				SETGPIO(teste)
				if status:
					print ("Song found now playing!")
					status = 0		
		except():
			GPIO.cleanup()
			print ("GPIO CLEAN")
			print ("Program Closed")
			break
		out.write(data)
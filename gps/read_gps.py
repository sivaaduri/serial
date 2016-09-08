import serial
ser=serial.Serial('COM15',baudrate=9600,  stopbits=1, timeout=1)
filess=open("GPS_assist.txt",'r')
try:
	ser.open()
except:
	print "error"
	
	
r=filess.read()
while(r):
	#ser.write(r)
	r=filess.read()
while(1):
	r=ser.readline()
	print r
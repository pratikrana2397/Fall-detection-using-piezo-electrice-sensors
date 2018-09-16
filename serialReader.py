import serial
import time
import way2sms


from_mobile_number = "9555777987"
password = "P7342B"
to_mobile_number = "9555777987"
message = "Help!"

ser = serial.Serial('/dev/ttyACM1')
ser.flushInput()

state = False;
while True:
	try:
		time.sleep(0.02)
		ser_bytes = ser.readline()
		decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
		print(decoded_bytes)
		if decoded_bytes == 1:
			q = way2sms.sms(from_mobile_number, password)

			print (q.send(to_mobile_number,message))

			q.logout()
	except:
		print(traceback.format_exc())


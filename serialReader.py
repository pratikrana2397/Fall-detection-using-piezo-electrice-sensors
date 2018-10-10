import serial
import time
import way2sms


from_mobile_number = ["9560703539", "9555777987","9910762037"]
password = ["W2299A", "P7342B","B2434G"]
to_mobile_number = "9560703539"
message = "Urgent Help Required!"

additional_mobile_numbers = ["9555777987","9910762037"]

port_number = input('Enter port number: ')
ser = serial.Serial('/dev/ttyACM' + str(port_number))
ser.flushInput()

additional_mobile_numbers = [x.strip() for x in str(input('Enter comma seperated mobile numbers: ')).split(',')]
print ('Registered numbers: ', additional_mobile_numbers)

while True:
	try:
		time.sleep(0.02)
		ser_bytes = ser.readline()
		decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
		print(decoded_bytes)
		if decoded_bytes == 1:
			worked = False
			for user, pw in zip(from_mobile_number,password):
				q = way2sms.sms(user, pw)
				for mob in additional_mobile_numbers:
					q.send(mob, message)
				if q.send(to_mobile_number,message): 
					worked = True
					print('Success')
				q.logout()
				if worked:
					break
	except:
		pass
		#print(traceback.format_exc())


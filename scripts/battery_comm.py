#!/usr/bin/env python
# license removed for brevity

import rospy
import sys
import serial
from battery_nh2054.msg import Battery

def BatteryInfo():

	s = serial.Serial('/dev/stml4', 9600)

	s.close()

	s.open()

	pub = rospy.Publisher('battery_status',Battery, queue_size = 10)
	rospy.init_node('batt_info',anonymous = True)
	msg = Battery()
	r = rospy.Rate(2)

	while not rospy.is_shutdown():

		s.write("0")


		Data = int(s.read(8).encode('hex'),16)
		msg.temperature = float((Data >> 48))/100
		msg.voltage = float(((Data & 0x0000FFFF00000000) >> 32))/100
		msg.current = float((Data & 0x00000000FFFF0000) >> 16)/1000
		msg.capacity = float(Data & 0x000000000000FFFF)/100

		print("Temperature: " + str(float((Data >> 48))/100) + " C")

		print("Voltage: "+str(float(((Data & 0x0000FFFF00000000) >> 32))/100)+ " V")

		print("Current: "+str(float((Data & 0x00000000FFFF0000) >> 16)/1000)+" A")

		print("Capacity: "+str((float(Data & 0x000000000000FFFF))/100)+" Ah")

		pub.publish(msg)
		r.sleep()

	s.close()

if __name__ == '__main__':
	try:
		BatteryInfo()
	except rospy.ROSInterruptException:
		pass

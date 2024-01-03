from dronekit import connect, VehicleMode
import time
import math
from pymavlink import mavutil
connection_string="127.0.0.1:14550"

iha=connect(connection_string, wait_ready=True, timeout=100)

def arm_ol_yuksel(hedef_yukseklik):
	while iha.is_armable==False:
		print("Arm için gerekli şartlar sağlanamadı")
		time.sleep(1)
	print("Iha su anda arm edilebilir")
	
	iha.mode=VehicleMode("GUIDED")
	while iha.mode=='GUIDED':
		print('Guided moduna gecis yapiliyor')
		time.sleep(1.5)
	
	print("Guided moduna gecis yapildi")
	iha.armed=True
	while iha.armed is False:
		print("Arm icin bekleniliyor")
		time.sleep(1)
	
	print("Iha arm oldu")
	
	iha.simple_takeooff(hedef_yukseklik)
	while iha.location.global_relative_frame.alt <= hedef_yukseklik *0.94:
		print("Su anki yukseklik {}".format(iha.location.global_relative_frame.alt))
		time.sleep(0.5)
	print("Takeoff gerceklesti")

def pozisyon(posx, posy, yaw_rate, posz, iha):
	msg = iha.message_factory.set_position_target_local_ned_encode(
	0,
	0, 0,
	mavutil.mavlink.MAV_FRAME_LOCAL_NED,
	0b0000011111111000,
	posx, posy, posz, # positions(meters)
	0, 0, 0, # Velocities(meters/seconds)
	0, 0, 0, # acceleration (your function)
	0, math.radians(yaw_rate)) # yaw, yaw_rate(radiant, radiant/second)
	
	iha.send_mavlink(msg)
	
	
arm_ol_yuksel(15)

pozisyon(5, 0, 0 ,-15 ,iha)
while iha.location.local_frame.north <= 4.90:
	print("5 metre kuzeye ilerliyorum")
	time.sleep(1)
print("Kuzeydeyim")
time.sleep(1)

pozisyon(5, 5, 0 ,-15 ,iha)
while iha.location.local_frame.east <= 4.90:
	print("5 metre doguya ilerliyorum")
	time.sleep(1)
print("Dogudayim")
time.sleep(1)

pozisyon(0, 5, 0 ,-15 ,iha)
while iha.location.local_frame.north => 0.1:
	print("5 metre guneye ilerliyorum")
	time.sleep(1)
print("Guneydeyim")
time.sleep(1)

pozisyon(0, 5, 0 ,-20 ,iha)
while iha.location.local_frame.down <= 19.80:
	print("5 metre daha yukariya ilerliyorum")
	time.sleep(1)
print("Yukaridayim")
time.sleep(1)


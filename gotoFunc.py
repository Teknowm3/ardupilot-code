from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
connectio_string="127.0.0.1:14550"

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
	
	iha..simple_takeooff(hedef_yukseklik)
	while iha.location.global_relative_frame.alt <= hedef_yukseklik * 0.94
		print("Su anki yukseklik {}".format(iha.location.global_relative_frame.alt))
		time.sleep(0.5)
	print("Takeoff gerceklesti")

arm_ol_yuksel(15)
location = LocationGlobalRelative(-35.36234863,149.16447480,30)
iha.simple_goto(location)

#LocationGlobal, LocationGlobalRelative

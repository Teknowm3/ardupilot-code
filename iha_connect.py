# NVDIA SESSION'a bağlamak için TCP/UDP portuyla dışarıyla ilişikiye geçiyor
# Ardupilot'a bu adreslerle bağlanabiliriz.
# ÇALIŞTIRMAK İÇİN python iha_connect.py
from dronekit import connect, VehicleMode
# 		bağlanmak için | arm edebilme ve uçma

connection_string="127.0.0.1:14550"

tha = connect(connection_string,wait_ready=True,timeout=100) #  timeout defaultda 30'dur çok gerekli değil timeout kısmı ama yaptık.

print(iha.location.global_relative_frame.alt)

def	be_armable():
	while iha.is_armable==false:
		print("FAILED TO ARM the iha !!!")
		time.sleep(3)
	print("Iha can be arm right now.")
	
	iha.mode=VehicleMode("GUIDED")
	while iha.mode=='GUIDED':
		print("Switching to GUIDED MODE...")
		time.sleep(1.5)
		
	print("Mode switched to GUIDED!")
	iha.armed = True
	while iha.armed is False:
		print("Waiting for arm...")
		time.sleep(1)
	
	print("Iha was armed.")
	
def	fly_up(target_height):
	
	iha.simple_takeoff(target_height)
	while iha.location.global_relative_frame.alt <= target_height * 0.94
		print("Height is: {}".format(iha.location.global_relative_frame.alt))
		time.sleep(0.5)
	print("Takeoff has taken place.")
	
	
be_armbale()
fly_up(30)


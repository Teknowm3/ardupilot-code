from dronekit import connect, VehicleMode

connection_string="127.0.0.1:14550"

tha = connect(connection_string,wait_ready=True,timeout=100)

print(iha.parameters['WPNAV_SPEED'])
iha.parameters['WPNAW_SPEED'] = 40
print("Parametre değeri değiştirildi yeni değer: {}".format(iha.parameters['WPNAV_SPEED']))

# PARAMETRE LINK : ardupilot.org/copter/docs/parameters.html#wpnav-parameters
# Dronekit ustunde: param show yapıp parametre değerlerini görebilirsin.

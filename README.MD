<center>
---------------===========----------------
Mobile/Signal simulator
---------------===========----------------
</center>
<br>
<br>
<center>
--====Description====--
</center>
<br>
<br>
This project simulate mobile devices & network base stations, connecting by signal_power compared to distance.
<br>
<br>
<center>
--===Project structure===--
</center>
<br> 
Directory - base_classses:
<br>
* base_station.py - responsible for the base_station obj
* user_equipment.py - responsible for the user_devices obj (mobile,tablet..etc..)
* station_with_position.py - helper base class to help couple base_station data for further use.

Directory - configuration
* devices_enum.py - Devices enum with signal_strength & name


Directory - handlers:
* base_stations_handler.py - inherits the base_station base class and add functionality
* controller.py - controls the simulator
* user_equipment_handler.py - inherits the user_equipment base class and add functionality
* network_handler.py - responsible for all network/packet related events

Directory - utils
* logger - responsible to the logs of the simulator
* tools - generic helper tools


main.py \
The Simulation runs from here


requirements.txt \
lib requirements


<center>
--===setup===--
</center>
<br>
<br>
pip install -r requirements.txt


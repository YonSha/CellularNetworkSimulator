import logging

from configuration.devices_enum import DeviceEnum
from handlers.controller import Controller

logging.info("Simulation started")
co = Controller()

co.init_stations(num_bs=3, bs_power=35)
co.add_equipment(id=1, position=(50, 50), device=DeviceEnum.GALAXY_S21, status="online",network_online=True)
co.move_eq(id=1, steps=3)
co.add_station(60)
co.add_equipment(id=2, position=(50, 50), device=DeviceEnum.IPAD_PRO, status="online", network_online=True)
co.move_eq(id=2, steps=4)

dev1 = co.return_device_by_id(1)
dev2 = co.return_device_by_id(2)

sender = co.init_network()
sender.run(sender_devices=[dev1], target_devices=[dev2], target_port=80, payload="Hello TCP", protocol='TCP')

co.create_plot()
co.show_plot()
logging.info("Simulation Ended")

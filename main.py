import logging

from configuration.devices_enum import DeviceEnum
from configuration.providers_enum import ProviderEnum
from handlers.controller import Controller

# TODO:
#  Add support for more than one signal types for devices
#  let devices see each other,
#  if device not connected to a cell tower, no packet sent
#  change provider into a class
#  add provider approved sims ( {sim num}:{active}/disabled
#  add provider provide sim generator
#  add provider support for private network (will require to add device signal strength support)
#  Airplan mode
#  fix overlapping texts in result map
logging.info("Simulation started")
co = Controller()

co.init_cell_towers(num_bs=3, provider=ProviderEnum.customer_one)
co.add_equipment(id=1, position=(50, 50), device=DeviceEnum.GALAXY_S22, status="online",network_online=True)
co.move_eq(id=1, steps=3)
co.add_cell_tower(ProviderEnum.customer_two)
co.add_equipment(id=2, position=(50, 50), device=DeviceEnum.IPAD_PRO, status="online", network_online=True)
co.move_eq(id=2, steps=4)

dev1 = co.return_device_by_id(1)
dev2 = co.return_device_by_id(2)

# sends packets between devices
co.init_network().run(sender_devices=[dev1], target_devices=[dev2], target_port=80, payload="Hello TCP", protocol='TCP')


co.create_plot()
co.show_plot()
logging.info("Simulation Ended")

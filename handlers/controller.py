import logging
import warnings
from matplotlib import pyplot as plt
from handlers.base_stations_handler import BaseStationsHandler
from handlers.provider_handler import ProviderHandler
from handlers.user_equipment_handler import UserEquipmentHandler
from handlers.network_handler import NetworkHandler
from utils.tools import generate_sim_code, generate_ip_addresses
import pandas as pd


class Controller:
    def __init__(self):
        self.eq_list = []
        self.equipment = None
        self.stations = None
        self.ip_address = 0
        self.plot_data = []

        self.plot_path = 'generated_files\plot.pdf'
        self.data_path = 'generated_files\plot_data.csv'

    # create new provider
    def create_new_provider(self, name, signals, status):
        return ProviderHandler(name, signals, status)

    def init_network(self):
        return NetworkHandler()

    def return_device_by_id(self, id):
        for eq in self.eq_list:
            if eq.id == id:
                logging.info(f"Returned Device OBJ -> id:{id}")
                return eq

    def add_equipment(self, id, position, device, status, network_online) -> None:
        signal_name, signal_strength = device.get_random_signal()
        self.ip_address = generate_ip_addresses(self.ip_address)
        sim_code = generate_sim_code()
        bs_data = self.stations.return_bs_data
        self.eq_list.append(
            UserEquipmentHandler(id, position=position, eq_class=device.device_name, status=status, bs_data=bs_data,
                                 sim_code=sim_code, signal_strength=signal_strength, signal_name=signal_name,
                                 ip_address=f"192.168.1.{self.ip_address}", network_online=network_online))
        logging.info(f"Added device id:{id}")

    # TODO: Add support for more than one signal types for devices, and let devices see each other
    def init_stations(self, num_bs=1, provider=None, id=None, position=None, status=None) -> None:
        signal_type, signal_strength = provider.get_random_signal_strength()

        logging.info(f"initiate base stations")
        self.stations = BaseStationsHandler(num_bs=num_bs, provider_name=provider.provider_name,
                                            signal_strength=signal_strength,
                                            signal_type=signal_type, supported_signals=provider.signals, id=id,
                                            position=position, status=status)

    def add_station(self, provider=None, status="online"):
        self.stations.add_base_station(provider, status)

    def move_eq(self, id, steps=5) -> None:
        for eq in self.eq_list:
            if eq.id == id:
                logging.info(f"Device ID:{id}, Moved {steps} steps")
                return eq.move(steps)

    def check_device_proximity(self):
        stations, positions = self.stations.return_bs_data
        for i in stations:
            print(i)

    def create_plot(self) -> None:
        warnings.filterwarnings("ignore")
        fig, ax = plt.subplots(figsize=(16, 16))

        # Define a list of distinct colors
        distinct_colors = [
            'green', 'blue', 'orange', 'purple',
            'cyan', 'magenta', 'yellow', 'brown', 'pink',
            'gray', 'lime', 'teal', 'navy', 'olive', 'coral'
        ]

        if len(self.eq_list) > len(distinct_colors):
            raise ValueError("Not enough distinct colors for the number of user equipment instances.")

        for i, eq in enumerate(self.eq_list):
            self.equipment = eq

            # Plot base stations
            if i == 0:
                ax.scatter(*zip(*self.stations.bs_positions), marker='^', color='red', label='Base Stations')

            # Plot user equipment position with distinct color
            ax.scatter(self.equipment.position[0], self.equipment.position[1],
                       color=distinct_colors[i], label=f'User Equipment {i + 1}', s=100)

            # Save the data for further CSV usage(test).
            self.plot_data.append({
                'User Equipment ID': eq.id,
                'X Position': self.equipment.position[0],
                'Y Position': self.equipment.position[1],
                'Sim Code': self.equipment.sim_code,
                'Trajectory': [(pos[0], pos[1], bs_id) for pos, bs_id in self.equipment.trajectory]
            })
            # bs data
            for bs in self.stations.stations_with_positions:
                ax.text(
                    bs.position[0],
                    bs.position[1] + 2,
                    f'BS{bs.base_station.id}({bs.base_station.provider_name})',
                    fontsize=6.5,
                    ha='center',
                    bbox=dict(facecolor='white', alpha=0.5, edgecolor='black', boxstyle='round,pad=0.3')
                )
                ax.text(
                    bs.position[0],
                    bs.position[1] - 3,
                    f'{bs.base_station.supported_signals}',
                    fontsize=6.5,
                    ha='center',
                    bbox=dict(facecolor='white', alpha=0.5, edgecolor='black', boxstyle='round,pad=0.3')
                )

            # Plot trajectory
            counter = 1
            for pos, bs_id in self.equipment.trajectory:
                ax.plot([pos[0]], [pos[1]], 'bo', color=distinct_colors[i])
                ax.text(
                    pos[0], pos[1] + 2,
                    f'EQ:{eq.id} -> BS: {bs_id} (step{counter})',
                    fontsize=6.5,
                    ha='center',
                    bbox=dict(facecolor='white', alpha=0.5, edgecolor='black', boxstyle='round,pad=0.3')
                )

                ax.text(
                    pos[0],
                    pos[1] - 3,
                    f'Sim:{self.equipment.sim_code}({self.equipment.signal_name})',
                    fontsize=6.5,
                    ha='center',
                    bbox=dict(facecolor='white', alpha=0.5, edgecolor='black', boxstyle='round,pad=0.3')
                )
                counter += 1
        # Set limits and labels
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_title('Cellular Network Simulation')
        ax.set_xlabel('X Position')
        ax.set_ylabel('Y Position')
        ax.grid()
        logging.info("Created PLOT for devices map")

    def show_plot(self) -> None:

        logging.info("Show device map")
        plt.rcParams['font.family'] = 'Arial'
        # Save the map created as a PDF file
        plt.savefig(self.plot_path, dpi=1000, bbox_inches='tight', pad_inches=0.1)
        # Save the data to a CSV file for further testing
        data_df = pd.DataFrame(self.plot_data)
        data_df.to_csv(self.data_path, index=False)
        plt.legend()
        plt.show()

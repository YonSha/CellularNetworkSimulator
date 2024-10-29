class CellTowerWithPosition:
    def __init__(self, cell_tower, position):
        self.cell_tower = cell_tower
        self.position = position

    def __repr__(self):
        return f"StationWithPosition(base_station={self.cell_tower}, position={self.position})"

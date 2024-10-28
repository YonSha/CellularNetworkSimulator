class StationWithPosition:
    def __init__(self, base_station, position):
        self.base_station = base_station
        self.position = position

    def __repr__(self):
        return f"StationWithPosition(base_station={self.base_station}, position={self.position})"

class Chair:

    def __init__(self, chair_coordinates):
        self.chair_coordinates = chair_coordinates
        self.TopLeft = chair_coordinates[0]
        self.Face = None

    def chair_is_occupied(self, x_coordinate, y_coordinate):
        return False

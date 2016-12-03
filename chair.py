from PIL import Image
import numpy as np


class Chair:

    def __init__(self, chair_coordinates, empty_chair_image):
        self.TopLeft = [chair_coordinates[0][0], chair_coordinates[0][1]]
        self.bottomRight = [chair_coordinates[1][0], chair_coordinates[1][1]]
        self.topRight = [self.bottomRight[0], self.TopLeft[1]]
        self.bottomLeft = [self.TopLeft[0], self.bottomRight[1]]
        self.chair_image = empty_chair_image
        #self.empty_chair_array = []
        self.empty_chair_array = np.zeros([self.bottomRight[1] - self.topRight[1], self.topRight[0] - self.TopLeft[0], 3], dtype=np.uint8)
        self.init_reference_image(empty_chair_image)
        self.Face = None

    def init_reference_image(self, empty_chair_image):
        y_ind = 0
        x_ind = 0
        for y in range(self.TopLeft[1], self.bottomLeft[1]):
            for x in range(self.TopLeft[0], self.topRight[0]):
                self.empty_chair_array[y_ind][x_ind] = empty_chair_image[y][x]
                x_ind += 1
            x_ind = 0
            y_ind += 1

    def display(self):
        img = Image.fromarray(self.empty_chair_array)
        img.show()

    def chair_is_occupied(self, x_coordinate, y_coordinate):
        return False

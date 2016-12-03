from chair import Chair
import sys
from PIL import Image
import numpy as np
from face import Face

empty_chairs_image = Image.open("chair_pictures/2students.bmp")
empty_chairs_array = np.array(empty_chairs_image)


#               top left corner  bottom right corner
auditorium = [Chair([[578, 386], [690, 537]], empty_chairs_array),   # top left
              Chair([[730, 391], [863, 555]], empty_chairs_array),   # top middle
              Chair([[923, 391], [1045, 555]], empty_chairs_array),  # top right
              Chair([[490, 531], [623, 719]], empty_chairs_array),   # bottom left
              Chair([[705, 522], [832, 728]], empty_chairs_array),   # bottom middle
              Chair([[900, 531], [1041, 737]], empty_chairs_array)]  # bottom right

# auditorium[0].empty_chair_array
auditorium[0].display()
auditorium[1].display()
auditorium[2].display()
auditorium[3].display()
auditorium[4].display()
auditorium[0].display()

#we would fill this in from the webcam, which returns XCoord, YCoord, Width, Height
Face.connectFacesAndChairs(auditorium, [Face(781, 319, 1, 1),   # kirsten
                                        Face(723, 455, 1, 1),  # tyler
                                        Face(623, 322, 1, 1)]) #fake face to test that would be sitting in top row left

print("test")

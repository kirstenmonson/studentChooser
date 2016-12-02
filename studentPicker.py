from chair import Chair
import sys

#               top left corner  bottom right corner
auditorium = [Chair([[578, 386], [690, 537]]),   # top left
              Chair([[730, 391], [863, 555]]),   # top middle
              Chair([[923, 391], [1045, 555]]),  # top right
              Chair([[490, 531], [623, 719]]),   # bottom left
              Chair([[705, 522], [832, 728]]),   # bottom middle
              Chair([[900, 531], [1041, 737]])]  # bottom right


chairStatus = "OCCUPIED" if class_chair.chair_is_occupied(1, 2) else "EMPTY"

print("The chair is", chairStatus)



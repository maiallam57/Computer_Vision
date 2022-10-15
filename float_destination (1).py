import cv2
import numpy as np
import argparse

# parser = argparse.ArgumentParser(description="Find Float Destination")
# parser.add_argument("speed", default=0.143, type=float, help="speed of float")
# parser.add_argument("direction", default=85, type=float, help="direection of float")
# parser.add_argument("time", default=144, type=float, help="time spent by float")
# args = parser.parse_args()


class FloatMap:
    def __init__(self) -> None:
        self.map = self.draw_map()
        self.cells_locations = []
        self.get_cells_locations()
        cv2.rectangle(self.map, *self.cells_locations[9][5], (0, 0, 0), -1)

    def draw_map(self):
        grid_image = np.ones((600, 1200, 3), dtype=np.uint8)*255

        for j in range(60, 560, 20):
            cv2.line(grid_image, (120, j), (1080, j), (128, 128, 128), 3)

        for i in range(120, 1100, 20):
            cv2.line(grid_image, (i, 60), (i,540), (128, 128, 128), 3)
        return grid_image

    def get_cells_locations(self):
        for i in range(60, 540, 20):
            current_locations = []
            for j in range(120, 1080, 20):
                current_locations.append([(j, i), (j+20, i+20)])
            self.cells_locations.append(current_locations)


class FloatDestination:
    def __init__(self, speed, direction, time) -> None:
        self.distance = speed*time*60*60
        self.y = self.distance*np.cos(direction*np.pi/180.)
        self.x = self.distance*np.sin(direction*np.pi/180.)

        self.y_direction = "north" if self.y > 0 else "south"
        self.x_direction = "east" if self.x > 0 else "west"
        
        self.distance = np.round(self.distance/1000, 3)
        self.y = np.round(abs(self.y)/1000, 2)
        self.x = np.round(abs(self.x)/1000, 2)
    

        self.y_delta = int(np.round(self.y/2))
        self.x_delta = int(np.round(self.x/2))

        self.new_y = 9 - self.y_delta if self.y_direction == "north" else 9 + self.y_delta
        self.new_x = 5 + self.x_delta if self.x_direction == "east" else 5 - self.x_delta

    def get_destination(self):
        return self.new_x, self.new_y

float_map = FloatMap()
float_map_image = float_map.map
float_map_cells = float_map.cells_locations

x, y = FloatDestination(0.117, 96, 144).get_destination()

cv2.rectangle(float_map_image, *float_map_cells[y][x], (0, 0, 255), -1)

# while True:
#     cv2.imshow("map", float_map_image)
#     key = cv2.waitKey(0)
# cv2.destroyAllWindows()        

cv2.imshow("map", float_map_image)
cv2.waitKey(0)
cv2.destroyAllWindows()    
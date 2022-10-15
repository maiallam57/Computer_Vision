import numpy as np 
import cv2

jhonsmith=cv2.imread("D:/vortex/MATE 2023/training phase/ms2/OpenCV2/Tasks/jhonsmith.jpg")
jhonsmith = cv2.resize(jhonsmith, (450,250))
h, w, c = jhonsmith.shape
circles=[]
counter=0
text=""
def draw_circle(event, x, y, flags, param):

    global circles, counter
    try:
        if event==cv2.EVENT_LBUTTONDOWN:
            circles.append((x, y))
            counter+=1
    except IndexError:
        print("only 4 points")

    if event == cv2.EVENT_RBUTTONDBLCLK: # Delete all circles
        circles[:] = []
        counter = 0
    elif event == cv2.EVENT_RBUTTONDOWN: # Delete last added circle
        try:
            circles.pop()
            counter-=1
        except (IndexError):
            print("no circles to delete")
        
dst_image = clone = jhonsmith.copy()
cv2.namedWindow('jhonsmith')
cv2.setMouseCallback('jhonsmith', draw_circle)

while True:
    image = clone.copy()
    key=cv2.waitKey(1)
    for pos in circles:
        cv2.circle(image,pos,3,(0,0,255),-1)
    if counter==4:
        points1=np.float32([circles[0],circles[1],circles[2],circles[3]])
        points2=np.float32([[0,0],[w,0],[0,h],[w,h]])                                
        matrix=cv2.getPerspectiveTransform(points1,points2)
        dst_image=cv2.warpPerspective(image,matrix,(w,h))                        
    if counter==0:
            text="choose upper left point"
            cv2.putText(image,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,255),1)    
    if counter==1:
        text="choose upper right point"    
        cv2.putText(image,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,255),1)    
    if counter==2:
        text="choose lower left point"
        cv2.putText(image,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,255),1)    
    if counter==3:
        text="choose lower right point" 
        cv2.putText(image,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,255),1)    
    
    im_v = cv2.vconcat([image, dst_image])
    cv2.imshow("jhonsmith", im_v)
    
    if key== ord('Q') or key== ord('q'):
          break

cv2.destroyAllWindows() 





















# import cv2
# import numpy as np

# font=cv2.FONT_HERSHEY_COMPLEX

# class FloatMap:
#     def __init__(self) -> None:
#         self.map = self.draw_map()
#         self.cells_locations = []
#         self.get_cells_locations()
#         cv2.rectangle(self.map, *self.cells_locations[9][5], (0, 0, 0), -1)

#     def draw_map(self):
#         grid_image = np.ones((600, 1200, 3), dtype=np.uint8)*255

#         for j in range(60, 560, 20):
#             cv2.line(grid_image, (120, j), (1080, j), (128, 128, 128), 3)

#         for i in range(120, 1100, 20):
#             cv2.line(grid_image, (i, 60), (i,540), (128, 128, 128), 3)

#         cv2.putText(grid_image,"W",(1115,325),font,1,0,2)
#         cv2.putText(grid_image,"E",(45,325),font,1,0,2)
#         cv2.putText(grid_image,"N",(600,35),font,1,0,2)
#         cv2.putText(grid_image,"S",(600,575),font,1,0,2)

#         return grid_image

#     def get_cells_locations(self):
#         for i in range(60, 540, 20):
#             current_locations = []
#             for j in range(120, 1080, 20):
#                 current_locations.append([(j, i), (j+20, i+20)])
#             self.cells_locations.append(current_locations)


# class FloatDestination:
#     def __init__(self, speed, direction, time) -> None:
#         self.distance = speed*time*60*60
#         self.y = self.distance*np.cos(direction*np.pi/180.)
#         self.x = self.distance*np.sin(direction*np.pi/180.)

#         self.y_direction = "north" if self.y > 0 else "south"
#         self.x_direction = "east" if self.x > 0 else "west"
        
#         self.distance = np.round(self.distance/1000, 3)
#         self.y = np.round(abs(self.y)/1000, 2)
#         self.x = np.round(abs(self.x)/1000, 2)
    

#         self.y_delta = int(np.round(self.y/2))
#         self.x_delta = int(np.round(self.x/2))

#         self.new_y = 9 - self.y_delta if self.y_direction == "north" else 9 + self.y_delta
#         self.new_x = 5 + self.x_delta if self.x_direction == "east" else 5 - self.x_delta

#     def get_destination(self):
#         return self.new_x, self.new_y


# float_map = FloatMap()
# float_map_image = float_map.map

# speed = float(input("Enter the speed: "))
# angle = float(input("Enter the angle: "))
# time = float(input("Enter the time: "))

# float_map_cells = float_map.cells_locations
# x, y = FloatDestination(speed, angle, time).get_destination()

# cv2.rectangle(float_map_image, *float_map_cells[y][x], (0, 0, 255), -1)

# cv2.imshow("map", float_map_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 


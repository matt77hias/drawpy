import cv2
import numpy as np

finished = False
img = np.ones((512, 512, 3))
points = []

def draw_point(event, x, y, flags, param):
    global finished, img, points
    if (not finished and event == cv2.EVENT_LBUTTONDOWN):
        points.append(np.array([x, y], dtype=int))
        if len(points) > 1:
            cv2.line(img, (points[-2][0], points[-2][1]), (points[-1][0], points[-1][1]), (0,0,255))
        cv2.circle(img, (x,y), 2, (0,0,255), -1)  
    if (not finished and event == cv2.EVENT_RBUTTONDOWN):
        if len(points) > 1:
            cv2.line(img, (points[-1][0], points[-1][1]), (points[0][0], points[0][1]), (0,0,255))
        finished = True
                      
def draw_points(fin=None, fout=None, callback=draw_point):
    global finished, img, points
    finished = False
    points = []
    if fin is not None:
        img = cv2.imread(fin)

    img_name = 'LMB to add point, RMB to close curve'
    cv2.namedWindow(img_name)
    cv2.setMouseCallback(img_name, callback)

    while cv2.getWindowProperty(img_name, 0) >= 0:
        cv2.imshow(img_name, img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
                
    if fout is not None:
        cv2.imwrite(fout, img)
            
    return points
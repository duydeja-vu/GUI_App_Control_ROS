#!/usr/bin/python3
import rospkg
import rospy
import sys
import os
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Float32
import cv2
import numpy as np
from ctypes import *
import math
import random
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.stats import itemfreq
from sensor_msgs.msg import Joy







def car_control(angle, speed):
    pub_speed = rospy.Publisher('/team706/set_speed', Float32, queue_size=10)
    pub_speed.publish(speed)
    # rate = rospy.Rate(100)
    pub_angle = rospy.Publisher('/team706/set_angle', Float32, queue_size=10)
    # if angle>0:
    #     angle += 3
    # if angle<0:
    #     angle -= 3
    pub_angle.publish(angle)
    print('Angle:', angle, 'Speed:', speed)
    # rate = rospy.Rate(100)



def rgb_to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    

def canny(img, low_threshold, high_threshold):
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def edges_detect(frame):
    gray_img = rgb_to_gray(frame)
    mask_white = cv2.inRange(gray_img, 150, 255)
    
    kernel_size = 5
    gauss_gray = gaussian_blur(mask_white,kernel_size)
    cv2.imshow("gray", mask_white)
    low_threshold = 50
    high_threshold = 150
    edges = canny(gauss_gray, low_threshold, high_threshold)
    cv2.imshow("canny", edges)
    return edges

def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)
    polygon = np.array([[
        (0, height * 1 / 2),
        (width, height * 1 / 2),
        (width, height),
        (0, height),
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)
    return cropped_edges

def detect_line_segments(cropped_edges):
    cv2.imshow("cropped_edges", cropped_edges)
    rho = 1 
    angle = np.pi / 180  
    min_threshold = 10
    line_segments = cv2.HoughLinesP(cropped_edges, rho, angle, min_threshold, 
                                    np.array([]), minLineLength=24, maxLineGap=4)
    return line_segments

def average_slope_intercept(frame, line_segments):
    lane_lines = []
    if line_segments is None:

        return lane_lines

    height, width, _ = frame.shape
    left_fit = []
    right_fit = []

    boundary = 1/3
    left_region_boundary = width * (1 - boundary)  
    right_region_boundary = width * boundary 

    for line_segment in line_segments:
        for x1, y1, x2, y2 in line_segment:
            if x1 == x2:
                continue
            fit = np.polyfit((x1, x2), (y1, y2), 1)
            slope = fit[0]
            intercept = fit[1]
            if slope < 0:
                if x1 < left_region_boundary and x2 < left_region_boundary:
                    left_fit.append((slope, intercept))
            else:
                if x1 > right_region_boundary and x2 > right_region_boundary:
                    right_fit.append((slope, intercept))

    left_fit_average = np.average(left_fit, axis=0)
    if len(left_fit) > 0:
        lane_lines.append(make_points(frame, left_fit_average))

    right_fit_average = np.average(right_fit, axis=0)
    if len(right_fit) > 0:
        lane_lines.append(make_points(frame, right_fit_average))



    return lane_lines

def make_points(frame, line):
    height, width, _ = frame.shape
    slope, intercept = line
    y1 = height  
    y2 = int(y1 * 1 / 2)  
    x1 = max(-width, min(2 * width, int((y1 - intercept) / slope)))
    x2 = max(-width, min(2 * width, int((y2 - intercept) / slope)))
    return [[x1, y1, x2, y2]]

def display_lines(frame, lines, line_color=(0, 255, 0), line_width=2):
    line_image = np.zeros_like(frame)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), line_color, line_width)
    line_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    return line_image


def detect_lane(frame, label, index):
    #os.chdir('/home/dejavu/team706_1/src/team706/src/after_preprocessing')
    edges = edges_detect(frame)
    cropped_edges = region_of_interest(edges)
    line_segments = detect_line_segments(cropped_edges)
    lane_lines = average_slope_intercept(frame, line_segments)
    

    depth_name = '{}_{}.jpg'.format(index, label)




x = y = 0.0
a_button = 0
start_gendata = False

def convert_to_angle(x, y):
    angle = 0.0
    if x == 0 and y == 0 or x == 0 and y > 0:
        angle = 0.0
    if x == 0.0 and y < 0.0:
        angle = 180.0
    if y == 0.0 and x > 0:
        angle = 90.0
    if y == 0.0 and x < 0:
        angle = -90.0
    elif x > 0.0 and y > 0.0:
        angle = math.degrees(math.atan(x/y))
    elif x > 0.0 and y < 0.0:
        angle = math.degrees(math.atan(x/y)) + 180.0
    elif x < 0.0 and y < 0.0:
        angle = math.degrees(math.atan(x/y)) - 180.0
    elif x < 0.0 and y > 0.0:
        angle = math.degrees(math.atan(x/y))
    if angle == -180 or angle == 180:
        angle = 0
    return float(angle)


rgb_index = 0
def image_callback(data):
    global rgb_index
    print(start_gendata)

    start_time = time.time()

    temp = np.fromstring(data.data, np.uint8)
    img = cv2.imdecode(temp, cv2.IMREAD_COLOR)
    frame = img
    angle = convert_to_angle(x, y)
    print(angle)
    car_control(angle=angle, speed=30)

    if start_gendata == True:
        rgb_index += 1
        if angle < 0.0:
            label = "left"
        elif angle > 0.0:
            label = "right"
        else:
            label = "forward"

        # if angle < 0.0 and angle >= -30.0:
        #     label = 0.0
        # if angle >= -60 and angle < -30.0:
        #     label = -30
        # if angle >= -90 and angle < -60.0:
        #     label = -60        
        # if angle >= 0.0 and angle <= 30.0:
        #     label = 0.0
        # if angle > 30 and angle <= 60.0:
        #     label = 30.0
        # if angle > 60.0 and angle <90 :
        #     label = 60.0
        rgb_name = '{}_{}.jpg'.format(rgb_index, label)
        detect_lane(frame, label, rgb_index)
        cv2.imwrite(rgb_name, frame)
    else:
        pass

    cv2.imshow("frame", frame)
    cv2.waitKey(1)
    print('FPS:', 1/(time.time() - start_time))
    
    


def joy_callback(joy_data):
    global x, y, a_button, start_gendata
    for index in range(len(joy_data.axes)):
        x = -(joy_data.axes[0])
        y = joy_data.axes[1]
    for index in range(len(joy_data.buttons)):
        a_button = joy_data.buttons[0]
        if a_button == 1:
            start_gendata = True if start_gendata == False else False

#     y_button = joy_data.buttons[3]
#     left_b = joy_data.buttons[4]
#     right_b = joy_data.buttons[5]
#     right_t = joy_data.buttons[7]
#     start_button = joy_data.buttons[9]
# if start_button == 1:
#     


def main():
    rospy.init_node('team706_node', anonymous=True)
    rospy.Subscriber("/team706/camera/rgb/compressed", CompressedImage,
    image_callback, queue_size=10, buff_size=2**24)
    joy_sub = rospy.Subscriber("joy", Joy, joy_callback)

    rospy.spin()
# video_out.release()
# print('Saved', video_out_name)



if __name__ == '__main__':
    main()

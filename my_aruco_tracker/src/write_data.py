#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
import csv


w = csv.writer(open('datafile.csv', 'a'))


def callback(data):
    w.writerow([data.header.seq, data.header.stamp, data.header.frame_id,
                data.pose.position.x, data.pose.position.y, data.pose.position.z,
                data.pose.orientation.x, data.pose.orientation.y, data.pose.orientation.z, data.pose.orientation.w])


def track_marker():
    rospy.init_node('tracking_data', anonymous=True)
    rospy.Subscriber('/aruco_single/pose', PoseStamped, callback)
    rospy.spin()


if __name__ == '__main__':
    print('Node to write tracked data started .......')
    w.writerow(['seq', 'time_stamp', 'frame_id', 'px', 'py', 'pz', 'qx', 'qy', 'qz', 'qw'])
    track_marker()

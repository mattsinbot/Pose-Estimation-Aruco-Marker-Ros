# Pose-Estimation-Aruco-Marker-ROS
6-DoF Pose Estimation using Aruco Markers in ROS

In order to estimate 6-DoF pose of Aruco markers in ROS, we needto follow the following steps,
1. Create ROS workspace
2. Clone usb_cam package
3. Calibrate the camera
4. Clone aruco_ros package
5. Create Aruco marker tracking package
6. Test tracking

Now that we know the basic steps required, we will explain each of the steps one by one.

### Create ROS workspace
The method to create ROS `catkin` workspace is well described in ROS documentation [here](http://wiki.ros.org/catkin/Tutorials/create_a_workspace). However for the completenes we will descrbe the process here as well. Please follow the instruction given below after you open a new terminal,

```
$ source /opt/ros/melodic/setup.bash
$ mkdir -p ~/ros_ws_cam/src
$ cd ~/catkin_ws/
$ catkin_make
```
Do not forget to `source` the new `*.sh` file now on every time you open a new terminal.
```
$ source devel/setup.bash
```

### Clone `usb_cam` package

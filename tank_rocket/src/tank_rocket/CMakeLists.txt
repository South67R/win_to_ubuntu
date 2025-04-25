cmake_minimum_required(VERSION 3.0.2)
project(tank_rocket)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  sensor_msgs
  urdf
  xacro
  gazebo_ros
  joint_state_publisher
  robot_state_publisher
  nav_msgs 
  tf2_ros
  gmapping
  map_server
)

catkin_package(
  CATKIN_DEPENDS 
  gmapping 
  map_server
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)



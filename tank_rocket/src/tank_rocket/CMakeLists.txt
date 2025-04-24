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
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Nếu có script python, có thể cài đặt như sau (tuỳ chọn):
# catkin_install_python(PROGRAMS scripts/control_keyboard.py
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

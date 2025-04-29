
# Tank_rocket Gmapping&Navigatio







## Created By

Thành viên nhóm:

- Nguyễn Văn Nam 
- Nguyễn Đình Cảnh Kỳ
- Lê Công Phú


# Install 

Mở 1 terminal 

```bash
  git clone https://github.com/South67R/win_to_ubuntu.git
```
Hãy cài đặt các package phù hợp để có thể sử dụng

```bash
  sudo apt-get install ros-noetic-joy \
  ros-noetic-teleop-twist-joy \
  ros-noetic-teleop-twist-keyboard \
  ros-noetic-amcl \
  ros-noetic-map-server \
  ros-noetic-move-base \
  ros-noetic-urdf \
  ros-noetic-xacro \
  ros-noetic-rqt-image-view \
  ros-noetic-gmapping \
  ros-noetic-navigation \
  ros-noetic-joint-state-publisher \
  ros-noetic-robot-state-publisher \
  ros-noetic-slam-gmapping \
  ros-noetic-dwa-local-planner \
  ros-noetic-joint-state-publisher-gui
```


```bash
  cd ~/tank_rocket && catkin_make 
```
# Các bước scan map bằng Gmapping 
```bash
  cd ~/tank_rocket && source devel/setup.bash 
```
Chạy mô phỏng Gazebo
```bash
  roslaunch tank_rocket tank_rocket_model.launch 
```
Chạy Teleop điều khiển 
```bash
  rosrun tank_rocket control_keyboard.py
```
Chạy mô phỏng Rviz 
```bash
  roslaunch tank_rocket rviz.launch 
```
Chạy package gmapping 
```bash
  rosrun gmapping slam_gmapping scan:=scan 
```
Trong Rviz hãy add thêm 2 topic sau vào:             
  ```bash
  /map 
  /scan 
```
Giờ thì hãy di chuyển Robot để scan map 

# Các bước chạy Navigation 
```bash
  cd ~/tank_rocket && source devel/setup.bash 
```
Chạy mô phỏng Gazebo
```bash
  roslaunch tank_rocket tank_rocket_model.launch 
```
Chạy file Navigation
```bash
  roslaunch tank_rocket_navigation tank_rocket_navigation.launch 
```
Giờ hãy chọn vào 2D Nav Goal trên tranh công cụ Rviz để xác định điểm muốn tới.

# Cảm ơn đã xem !!!

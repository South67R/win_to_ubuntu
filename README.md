
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

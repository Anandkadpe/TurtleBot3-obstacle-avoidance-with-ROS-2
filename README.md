# 🐢 TurtleBot3 Obstacle Avoidance (ROS 2)
A simple ROS 2 project to simulate obstacle avoidance behavior for TurtleBot3 using LiDAR data in the Gazebo simulation environment.

![2025-05-0516-41-19-ezgif com-video-to-gif-converter (1)]


## 📦 Features
- Obstacle detection using /scan (LaserScan) data
- Simple reactive avoidance using velocity commands
- ROS 2 launch support
- Easy to extend with advanced logic

## 🧱 Requirements
- Ubuntu 22.04
- ROS 2 Humble
- Gazebo
- TurtleBot3 packages

## 🚀 Getting Started
1. Clone this repository into your ROS 2 workspace
   
  	```
   cd ~/ros2_ws/src
   git clone https://github.com/Anandkadpe/TurtleBot3-obstacle-avoidance-with-ROS-2.git
   cd ..
   colcon build
   source install/setup.bash
    ```
2. Install TurtleBot3 simulation
      
  	```
	sudo apt update
	sudo apt install ros-humble-turtlebot3* -y
	echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc
	source ~/.bashrc
    ```
3. Launch simulation world
      
  	```
	ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
    ```
4. Launch obstacle avoidance node
      
  	```
	ros2 launch turtlebot3_obstacle_avoidance obstacle_avoidance.launch.py
    ```
## 📁 Project Structure
```
turtlebot3_obstacle_avoidance/
├── launch/
│   └── obstacle_avoidance.launch.py
├── turtlebot3_obstacle_avoidance/
│   └── obstacle_avoidance_node.py
├── package.xml
├── setup.py
├── setup.cfg
└── README.md
```

## 🧠 Logic Overview
- The node subscribes to /scan (LaserScan) topic, checks distances in the front region, and:
- Moves forward if clear
- Turns if an obstacle is too close

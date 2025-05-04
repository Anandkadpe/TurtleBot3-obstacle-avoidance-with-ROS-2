from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot3_obstacle_avoidance',
            executable='obstacle_avoidance_node',
            name='obstacle_avoidance_node',
            output='screen'
        )
    ])

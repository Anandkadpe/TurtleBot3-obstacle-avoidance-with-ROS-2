import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')
        self.subscriber = self.create_subscription(LaserScan, '/scan', self.laser_callback, 10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info("Obstacle Avoider Node Started")

    def laser_callback(self, msg):
        front_range = min(min(msg.ranges[0:10] + msg.ranges[-10:]), 10.0)
        twist = Twist()
        
        if front_range < 0.5:
            twist.angular.z = 0.5  # Turn
        else:
            twist.linear.x = 0.2   # Go forward

        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

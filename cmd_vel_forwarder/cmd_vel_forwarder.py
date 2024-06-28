#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdVelForwarder(Node):
    def __init__(self):
        super().__init__('cmd_vel_forwarder')
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.callback,
            10)
        self.publisher = self.create_publisher(Twist, '/diff_cont/cmd_vel_unstamped', 10)

    def callback(self, msg):
        # Create a new Twist message to publish
        new_msg = Twist()
        new_msg.linear = msg.linear
        new_msg.angular = msg.angular
        self.publisher.publish(new_msg)

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelForwarder()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotListener(Node):
    def __init__(self):
        super().__init__("robot_listener")
        self.robot_sub = self.create_subscription(
            String, "data_publisher", self.robot_sub_callback, 10)
        self.counter = 0
        self.get_logger().info("Robot is listening to the data_publihser topic...")

    def robot_sub_callback(self, msg):
        self.counter += 1
        self.get_logger().info(msg.data + str(self.counter))


def main(args=None):
    rclpy.init(args=args)
    node = RobotListener()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

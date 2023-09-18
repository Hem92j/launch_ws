import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SensorPublisher(Node):
    def __init__(self):
        super().__init__("sensor_publisher")
        self.sensor_pub_ = self.create_publisher(String, "data_publisher", 10)
        self.sensor_timer =   self.create_timer(1.0, self.sensor_timer_callback)
        self.get_logger().info("Sensor publisher is publishing string data....")

    def sensor_timer_callback(self):
        msg = String()
        msg.data = "I am publishing sensor data in String format..."
        self.sensor_pub_.publish(msg)


def main(args= None):
    rclpy.init(args=args)
    node = SensorPublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
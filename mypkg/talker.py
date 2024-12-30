import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.create_timer(1.0, self.cb)
        self.current_number = 2

    def cb(self):
        while not self.is_prime(self.current_number):
            self.current_number += 1
        msg = Int16()
        msg.data = self.current_number
        self.pub.publish(msg)
        self.get_logger().info(f"Published prime: {msg.data}")
        self.current_number += 1

    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True


def main():
    rclpy.init()
    node = Talker()
    try:
        rclpy.spin(node)
    except keyboardInterrupt:
        pass
    finally:
        node.destroy_node()
    rclpy.shutdown()

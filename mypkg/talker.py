import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.create_timer(1.0, self.cb)
        self.number = 2

    def cb(self):
        while not self.is_prime(self.number):
            self.number += 1
        msg = Int16()
        msg.data = self.number
        self.pub.publish(msg)
        self.get_logger().info(f"Sending prime: {self.number}")
        self.number += 1

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)

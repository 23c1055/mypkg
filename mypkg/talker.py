import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.create_timer(1, self.cb)
        self.number = 2

    def cb(self):
        while not self.prime(self.number):
            self.number += 1
        self.pub.publish(Int16(data=self.number))
        self.number += 1

    def prime(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)


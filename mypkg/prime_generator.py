import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Prime(Node):
    def __init__(self):
        super().__init__("prime")
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.timer = self.create_timer(1.0, self.cb)
        self.n = 2

    def cb(self):
        if self.is_prime(self.n):
            msg = Int16()
            msg.data = self.n
            self.pub.publish(msg)
            self.get_logger().info(f"prime: {self.n}")
        self.n += 1

    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True


def main():
    rclpy.init()
    node = Prime()
    try:
        rclpy.spin(node)
    except rclpy.executors.ExternalShutdownException:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()

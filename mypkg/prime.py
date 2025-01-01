import rclpy
from rclpy.node import Node


class Prime(Node):
    def __init__(self):
        super().__init__("prime")
        self.create_timer(1.0, self.cb)
        self.current_number = 2

    def cb(self):
        if self.current_number <= 200:
            if self.is_prime(self.current_number):
                self.get_logger().info(f"Prime: {self.current_number}")
            self.current_number += 1
        else:
            self.get_logger().info("Completed finding primes up to 200.")
            self.get_clock().cancel_timer(self.timer)

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

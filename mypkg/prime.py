import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random


class Prime(Node):
    def __init__(self, max_number=200):
        super().__init__(f"prime_{random.randint(0, 10000)}")
        self._timer = self.create_timer(1.0, self.cb)
        self._publisher = self.create_publisher(Int32, "prime_numbers", 10)
        self._current_number = 2
        self._max_number = max_number
        self.get_logger().info(f"Node initialized. Finding primes up to {self._max_number}.")

    def cb(self):
        if self._current_number <= self._max_number:
            if self.is_prime(self._current_number):
                self.get_logger().info(f"prime: {self._current_number}")
                msg = Int32()
                msg.data = self._current_number
                self._publisher.publish(msg)
            self._current_number += 1
        else:
            self.get_logger().info("Completed finding primes.")
            self._timer.cancel()
            self.shutdown()

    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    def shutdown(self):
        self.get_logger().info("Shutting down node.")
        self.destroy_node()
        rclpy.shutdown()


def main():
    rclpy.init()
    max_number = 200
    node = Prime(max_number)
    try:
        rclpy.spin(node)
    except rclpy.executors.ExternalShutdownException:
        pass
    finally:
        if rclpy.ok():
            node.shutdown()


if __name__ == "__main__":
    main()

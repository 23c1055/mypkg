# SPDX-FileCopyrightText: 2025 Goto Shingo
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Prime(Node):
    def __init__(self):
        super().__init__("published_prime")
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.timer = self.create_timer(1.0, self.cb)
        self.primes = self.generate_primes(10000)
        self.index = 0

    def cb(self):
        if self.index < len(self.primes):
            msg = Int16()
            msg.data = self.primes[self.index]
            self.pub.publish(msg)
            self.get_logger().info(f"{self.primes[self.index]}")
            self.index += 1

    def generate_primes(self, limit):
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        return [i for i, is_prime in enumerate(sieve) if is_prime]

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

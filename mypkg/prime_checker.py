# SPDX-FileCopyrightText: 2025 Goto Shingo
# SPDX-License-Identifier: BSD-3-Clause

# SPDX-FileCopyrightText: 2025 Goto Shingo
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Prime_Checker(Node):
    def __init__(self):
        super().__init__("prime_checker")
        self.pub = self.create_publisher(String, "prime_check", 10)
        self.timer = self.create_timer(1.0, self.cb)
        self.count = 1

    
    def cb(self):
        msg = String()
        msg.data = str(self.count)
        self.pub.publish(msg)

        prime_status = '〇' if self.is_prime(self.count) else '×'
        
        self.get_logger().info(f"{self.count} {prime_status}")
        self.count += 1

    
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


def main():
    rclpy.init()
    node = Prime_Checker()
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

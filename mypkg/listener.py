import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.pub = self.create_subscription(Int16, "countup", self.cb, 10)
    
    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.node.get_logger().info("Listen: %d" % msg.data)

def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
    
#rclpy.init()
#node = Node("listener")


#def cb(msg):
#    global node
#    node.get_logger().info("Listen: %d" % msg.data)


#def main():
#    pub = node.create_subscription(Int16, "countup", cb, 10)
#    rclpy.spin(node)

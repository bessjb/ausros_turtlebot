import rclpy
from rclpy.node import Node
import py_trees 

class PlanToNextUnknown(py_trees.behaviour.Behaviour):
    def __init__(self, name="PlanToNextUnknown", map_name="/battery/state"):
        super(ExampleAction, self).__init__(name=name)
        self.blackboard = self.attach_blackboard_client(name="PlanToNextUnknown") 
        self.blackboard.register_key(key="map",access=pytrees.common.Access.READ)

    def initialise(self):
        self.logger.info("Initialising Example Action")

    def update(self):
        if self.blackboard.example_key is True:
            self.logger.info("Example Action: Success")
            return py_trees.common.Status.SUCCESS
        else:
            self.logger.info("Example Action: Running")
            return py_trees.common.Status.RUNNING


class ExecutiveControl(Node):
    def __init__(self):
        super().__init__('behavior_node')
        self.get_logger().info("Initializing the behavior node")

        # Set up the py_trees behavior tree
        root = py_trees.composites.Selector("Root")
        plan_to_next_unknown = PlanToNextUnknown()
        root.add_child(plan_to_next_unknown)

        self.tree = py_trees.trees.BehaviourTree(root)

        # Timer to periodically "tick" the tree
        self.timer = self.create_timer(1.0, self.tick_tree)

    def tick_tree(self):
        self.get_logger().info("Ticking the behavior tree")
        self.tree.tick_once()

def main(args=None):
    rclpy.init(args=args)

    behavior_node = ExecutiveControl()

    rclpy.spin(behavior_node)

    behavior_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

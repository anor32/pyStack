import unittest


from Stack import Stack,Node


class TestNode(unittest.TestCase):
    node = Node("1")
    def test_init_Node(self):
        node = Node("1")
        self.assertEqual(self.node.data,"1")
        self.assertEqual(self.node.next_node,None)
        node_2 = Node(3,self.node)
        self.assertEqual(node_2.next_node, self.node)
        self.assertEqual(node_2.next_node.data, "1")


class TestStack(unittest.TestCase):
    stack = Stack(2)

    def test_init_stack(self):
        self.assertEqual(self.stack.stack_size,2)
        self.assertEqual(self.stack.top,None)

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.top.data,2)
        self.assertEqual(self.stack.top.next_node.data,1)
        self.assertEqual(self.stack.push(3), "Стэк переполнен")


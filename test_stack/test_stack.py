import unittest



from Stack import Stack, Node


class TestNode(unittest.TestCase):
    node = Node("1")

    def test_init_Node(self):
        node = Node("1")
        self.assertEqual(self.node.data, "1")
        self.assertEqual(self.node.next_node, None)
        node_2 = Node(3, self.node)
        self.assertEqual(node_2.next_node, self.node)
        self.assertEqual(node_2.next_node.data, "1")


class TestStack(unittest.TestCase):
    stack = Stack(2)

    def test_init_stack(self):
        self.stack.clear_stack()
        self.assertEqual(self.stack.stack_size, 2)
        self.assertEqual(self.stack.top, None)
        self.assertEqual(self.stack.size_stack(),0)

    def test_push(self):
        self.stack.clear_stack()
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.top.data, 2)
        self.assertEqual(self.stack.top.next_node.data, 1)
        self.assertEqual(self.stack.push(3), "Стэк переполнен")


    def test_pop(self):
        self.stack.clear_stack()
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.pop(), "Стэк пуст")

    def test_is_empty(self):
        self.stack.clear_stack()
        self.assertEqual(self.stack.is_empty(),True)

        self.stack.push(1)
        self.assertEqual(self.stack.is_empty(), False)


    def test_is_full(self):
        self.stack.clear_stack()
        self.stack.pop()
        self.assertEqual(self.stack.stack_size,2)
        self.assertEqual(self.stack.size_stack(), 0)
        self.assertEqual(self.stack.is_full(),False)
        self.stack.push(1)
        self.stack.push(1)
        self.assertEqual(self.stack.is_full(),True)

    def test_clear_stack(self):
        self.stack.clear_stack()
        self.stack.push(1)
        self.assertEqual(self.stack.size_stack(), 1)
        self.stack.clear_stack()
        self.assertEqual(self.stack.size_stack(),0)

    def test_get_data(self):
        self.stack.clear_stack()
        self.stack.push(1)
        print(self.stack.size_stack())
        self.assertEqual(self.stack.get_data(3), "Out of range")
        self.assertEqual(self.stack.get_data(0),1)


    def test_size_stack(self):
        self.stack.clear_stack()
        self.assertEqual(self.stack.size_stack(),0)
        self.stack.push(1)
        self.assertEqual(self.stack.size_stack(), 1)

    def test_counter_int(self):
        self.stack.clear_stack()
        self.stack.push(1)
        self.stack.push("2")
        self.assertEqual(self.stack.counter_int(), 1)
        self.stack.pop()
        self.stack.push(1)
        self.assertEqual(self.stack.counter_int(), 2)


#я незнаю почему но почему то когда я просто писал тесты где большую часть времени у меня все работало
# потом в какой то момент когда я писал метод test_get data и ошибки у меня начинали появляться вообще в ините я не понял почему
# я не нашел решения лучше кроме как очищать  стек в каждом вызове тогда все ок даже в ините
# если убрать всю очистку стека то можно заметить что стек в каждом методе все равно пустой
# либо я как то не так смотрел но у меня он показывал что он пуст

# может это специфика этого кода  я так и не понял почему у меня ошибка вообще была в ините
# ну я понял что стек не пустой передается поэтому ошибка была скорее всего
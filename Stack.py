class Node:
    """основной класс для связывания узлами принимает текущий узел и следующий"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    """класс  Стек для хранения элементов внутри инциализируется размером и верхним элементом"""

    def __init__(self, stack_size=5, top=None):
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    """добавления элемента в стек принимает элемент добавляет в стек"""

    def push(self, data):
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            # print("Стэк переполнен")
            return "Стэк переполнен"

    """удаление элемента из стека принимает элемент удаляет его"""

    def pop(self):
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    """проврека на то пуст ли стек возвращает true или false"""

    def is_empty(self):
        if self.top:
            return False
        else:
            return True

    """проврека на то полон ли стек возвращает true или false"""

    def is_full(self):
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    """очистка стека пока полный удаляет элементы """

    def clear_stack(self):
        while self.top:
            self.pop()

    """получение элемента по индесу принимает индекс возвращает элемент"""

    def get_data(self, index):
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    """получение длины стека возвращает длину стека"""

    def size_stack(self):
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    """подсчет целых чисел возвращает количество  целых чисел """

    def counter_int(self):
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter

# постарался по принципу 3 вопросов (что делает что принмает что возвращает) писать докстринги который вы сказали в конце урока
# я могу конечно детальнее расписать что делает каждый метод но как я понял лучше кратко писать

# почему то у меня тестах  из теста в тест stack обнуляется и там не сохраняются элементы внутри него только внутри начальной функции

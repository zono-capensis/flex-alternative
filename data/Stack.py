class Stack:
    def __init__(self):
        self.head = Node("Head")
        self.top = 0
    def get_size(self):
        return self.top
    def is_empty(self):
        return self.top == 0
    def peek(self):
        if self.is_empty():
            raise Exception("It's empty");
        return self.head.next.get_value();
    def pop(self):
        if self.is_empty():
            raise Exception("It's empty");
        current_node = self.head.next;
        self.head.next = self.head.next.next;
        self.top -= 1
        return current_node.get_value();
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head.next;
        self.head.next = new_node;
        self.top+= 1;
    def __str__(self):
        current_node = self.head.next;
        to_print = "["
        while current_node:
            to_print += (str(current_node.get_value()) + ",");
            current_node = current_node.next;
        to_print += "]"
        return to_print;

#Задача J
class Stack:
    a = []

    def push(self, item):
        self.a.append(item)

    def pop(self):
        return self.a.pop()

    def is_empty(self):
        return self.a == []
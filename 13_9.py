#Задача I
class Queue:
    a = []

    def push(self, item):
        self.a.append(item)

    def pop(self):
        return self.a.pop(0)

    def is_empty(self):
        return self.a == []
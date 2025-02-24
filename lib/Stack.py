class Stack:

    def __init__(self, items = [], limit = 100):
        if items is None:
            self.items = []
        else:
            self.items = list(items)
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:  
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None  
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        for i, item in enumerate(reversed(self.items)):
            if item == target:
                return i
        return -1

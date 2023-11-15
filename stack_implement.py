class Stack:
    def __init__(self, a=10):
        self.stack = []
        self.size = a
        self.top = 0


    def isFull(self):
        if self.top == self.size:
            return True
        return False


    def isEmpty(self):
        if self.top == 0:
            return True
        return False

    def push(self, a):
        if self.isFull():
            print("Stack Overflow!!!!!")
            return
        self.stack.append(a)
        print(f"{a} qo'shildi")
        self.top += 1


    def pop(self):
        if self.isEmpty():
            print("Stack Underflow!!!")
            return
        self.top -= 1
        print(f"{self.stack[-1]} o'chirildi!")
        self.stack.pop()


    def top(self):
        if self.isEmpty():
            print("Stack is Empty!!!!!")
            return
        return self.stack[-1]


s = Stack(5)
s.push(25)
s.push(30)
s.push(1)
s.pop()
s.pop()
s.pop()
s.pop()








class stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def peek(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            print(self.stack)
            print("top element:",self.stack[-1])
a=stack() 
a.push(10)
a.push(20)
a.push(30)

a.peek()

from NewStack import NewStack

stack = NewStack()
stack.push(9)
stack.push(24)
stack.push(15)
stack.push(2)
stack.push(7)

print("top element:", stack.top())
print("popped item:", stack.pop())
print("top element:", stack.top())

stack1 = NewStack()
print("popped item:", stack1.pop())

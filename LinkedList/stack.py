# Creating a stack in python



def create_stack():
  stack=[]
  return stack


#check for empty stack
#returns boolean
def check_empty(stack):
  return len(stack)==0


#add items to the stack
def push(stack,item):
  stack.append(item)
  print('pushed item ' + item)

#remove elements from the stack
def pop(stack):
  if(check_empty(stack)):
    return 'Stack is empty'

  return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item:" + pop(stack))
print("stack after popping an element: " + str(stack))


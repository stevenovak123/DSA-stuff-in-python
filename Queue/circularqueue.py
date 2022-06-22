# Circular Queue implementation in Python

class Circularqueue:


  def __init__(self,k):
    """
    k is the size of the queue
    queue is defined as a list with a length of k with null value
    """
    self.k=k
    self.queue=[None]*k
    self.head=self.tail=-1

  def enqueue(self,data):
    if((self.tail+1)%self.k == self.head):
      print("Circular queue is full")

    elif (self.head==-1):
      """
      if head ==-1 means start of the queue
      increment both by 1 and
      queue[tail]=data
      """
      self.head=0
      self.tail=0
      self.queue[self.tail]=data

    else:
      self.tail=(self.tail+1)%self.k
      self.queue[self.tail]=data

  #* Delete an item
  def dequeue(self):
    if(self.head==-1):
      print("Circular queue is empty\n ")
    elif(self.head==self.tail):
      temp=self.queue[self.head]
      self.head=-1
      self.tail=-1
      return temp
    else:
      temp=self.queue[self.head]
      self.head=(self.head+1)% self.k
      return temp

  def printCQueue(self):
    if(self.head==-1):
      print("No element in the queue")
    elif(self.tail>=self.head):
      for i in range(self.head,self.tail+1):
        print(self.queue[i], end=" ")
      print("\n")
    else:
      for i in range(self.head,self.k):
        print(self.queue[i],end=" ")
      for i in range(0, self.tail+1):
        print(self.queue[i],end=" ")
      print("\n")

obj=Circularqueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()
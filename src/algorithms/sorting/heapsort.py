

class heap:
  
  def __init__(self, size):
    self.size = size
    self.arr = []
    
  def insert(self, value):
    self.arr.append(value)
      
  def left(self, i):
    return 2*i 
  
  def right(self, i):
    return 2*i + 1
  
  def pprint(self):
    print(self.arr)
  
  def max_heapify(self, i): # some issue here
    l = self.left(i)
    r = self.right(i)
    if l < len(self.arr) and self.arr[l] > self.arr[i]:
      largest = l
    else: 
      largest = i
    if r <= len(self.arr) and self.arr[r] > self.arr[largest]:
      largest = r
    if largest != i:
      self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
      self.max_heapify(largest)
      
      
h = heap(11)
h.insert(1)
h.insert(3)
h.insert(5)
h.insert(1)
h.insert(6)
h.max_heapify(1)
h.pprint()
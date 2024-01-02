class CountdownIterator:
   def __init__(self, start):
     self.start = start
     self.current = start

   def __iter__(self):
     return self
   def __next__(self):
      if self.current < 0:
        raise StopIteration
      value = self.current
      self.current -= 1
      return value

start_value = 10
countdown = CountdownIterator(start_value)
for i in countdown:
  print(i)
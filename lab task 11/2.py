class StringIterator:
   def __init__(self, string):
    self.string = string
    self.index = 0  # Keep track of the current character index
   def __iter__(self):
     return self  # Return the iterator object itself
   def __next__(self):
     if self.index >= len(self.string):
       raise StopIteration  # Signal the end of iteration
     char = self.string[self.index]
     self.index += 1
     return char

test_string = "Hello, world!"
string_iterator = StringIterator(test_string)
for char in string_iterator:
  print(char)
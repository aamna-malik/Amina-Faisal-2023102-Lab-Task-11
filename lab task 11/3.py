class PowersOfTwoIterator:
  def __init__(self, start, end):
    if start <= 0:
      raise ValueError("Start value must be positive.")
    self.current_power = 0
    self.current_value = 1 
    self.end = end
  def __iter__(self):
    return self
  def __next__(self):
    if self.current_value > self.end:
      raise StopIteration
    value = self.current_value
    self.current_power += 1
    self.current_value *= 2
    return value

iterator = PowersOfTwoIterator(2, 32)
for value in iterator:
  print(value)
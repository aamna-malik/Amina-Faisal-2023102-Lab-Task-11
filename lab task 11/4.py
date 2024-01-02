class PrimeIterator:
  def __init__(self, end):
    if end <= 1:
      raise ValueError("End value must be greater than 1.")
    self.current = 2
    self.end = end
  def __iter__(self):
    return self
  def __next__(self):
    if self.current > self.end:
      raise StopIteration
    while not self.is_prime(self.current):
      self.current += 1
    prime = self.current
    self.current += 1
    return prime
  def is_prime(self, n):
    if n <= 1:
      return False
    for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
        return False
    return True

iterator = PrimeIterator(100)
for prime in iterator:
  print(prime)

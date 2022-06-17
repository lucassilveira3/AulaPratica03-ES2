class MemoryCalculator:
  
  def __init__(self, save_last_sum=False):
    self._sum = 0
    self._save_last_sum = save_last_sum
    self.last_sum = None

  def add(self, number):
    self._sum += number

  def sum(self):
    if self._save_last_sum:
      self.last_sum = self._sum
    temp = self._sum
    self._sum = 0
    return temp

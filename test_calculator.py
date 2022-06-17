import unittest
from calculator import MemoryCalculator

class TestMemoryCalculator(unittest.TestCase):

  def test_sum_is_zero_on_initialization(self):
    calculator = MemoryCalculator()
    self.assertEqual(0, calculator.sum())

  def test_sum_one_number(self):
    calculator = MemoryCalculator()
    calculator.add(2)
    self.assertEqual(2, calculator.sum())

  def test_sum_two_numbers(self):
    calculator = MemoryCalculator()
    calculator.add(2)
    calculator.add(3)
    self.assertEqual(5, calculator.sum())

  def test_sum_is_zero_after_calling_sum(self):
    calculator = MemoryCalculator()
    calculator.add(2)
    calculator.sum()
    self.assertEqual(0, calculator.sum())

  def test_sum_numbers_and_save_last_sum(self):
    calculator = MemoryCalculator()
    calculator.add(2)
    calculator.add(5)
    calculator._save_last_sum = True
    calculator.sum()
    calculator.add(5)
    self.assertEqual(7, calculator.last_sum)
    

from exercises.stringops import *
import unittest

class TestStringOps(unittest.TestCase):
  
  def test_reverse(self):
    self.assertEqual('olleh', reverse('hello'))
    self.assertEqual('12345', reverse('54321'))
    
  def test_has_unique_chars(self):
    self.assertTrue(has_unique_chars('world'))
    self.assertFalse(has_unique_chars('hello'))
    
if __name__ == '__main__':
    unittest.main()
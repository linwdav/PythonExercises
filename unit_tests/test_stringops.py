from exercises.stringops import *
import unittest

class TestStringOps(unittest.TestCase):
  
  def test_reverse(self):
    self.assertEqual('olleh', reverse('hello'))
    self.assertEqual('12345', reverse('54321'))
    self.assertEqual('lol', reverse('lol'))
    
  def test_has_unique_chars(self):
    self.assertTrue(has_unique_chars('world'))
    self.assertFalse(has_unique_chars('hello'))
    self.assertFalse(has_unique_chars('lol'))
    
  def test_is_substring(self):
    self.assertTrue(is_substring('h', 'h'))
    self.assertTrue(is_substring('he', 'hello'))
    self.assertFalse(is_substring('hello!', 'hello'))
    self.assertFalse(is_substring('helo', 'hello'))
    self.assertFalse(is_substring('hello', 'world'))
  
if __name__ == '__main__':
    unittest.main()
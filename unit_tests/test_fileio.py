from exercises.fileio import *
import unittest

class TestFileIO(unittest.TestCase):
  
  def test_read_write(self):
    filename = 'sample.txt'
    inputlist = ['hello', 'world']
    write_to_file(filename, inputlist)
    outputlist = read_from_file(filename)
    self.assertEquals('hello', outputlist[0])
    self.assertEquals('world', outputlist[1])
  
if __name__ == '__main__':
    unittest.main()
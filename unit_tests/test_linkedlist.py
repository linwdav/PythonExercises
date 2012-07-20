from exercises.linkedlist import LinkedList
import unittest

class TestLinkedList(unittest.TestCase):
  
  def test_insert(self):
    linkedlist = LinkedList()
    linkedlist.insert(1)
    linkedlist.insert(2)
    linkedlist.insert(3)
    nodeptr = linkedlist.head
    for i in range(1, 4, 1):
      self.assertEquals(i, nodeptr.value)
      nodeptr = nodeptr.next
      
  def test_clear(self):
    linkedlist = LinkedList()
    linkedlist.insert(1)
    linkedlist.insert(2)
    self.assertEquals(1, linkedlist.head.value)
    linkedlist.clear()
    self.assertEquals(None, linkedlist.head)
  
  def test_delete(self):
    linkedlist = LinkedList()
    self.assertEquals(0, linkedlist.delete(5))
    
    linkedlist.insert(1)
    self.assertEquals(1, linkedlist.head.value)
    self.assertEquals(1, linkedlist.delete(1))
    self.assertEquals(None, linkedlist.head)
    linkedlist.clear()
    
    linkedlist.insert(1)
    linkedlist.insert(2)
    self.assertEquals(1, linkedlist.delete(1))
    self.assertEquals(2, linkedlist.head.value)
    linkedlist.clear()
    
    linkedlist.insert(1)
    linkedlist.insert(2)
    linkedlist.insert(3)
    self.assertEquals(1, linkedlist.delete(2))
    self.assertEquals(1, linkedlist.head.value)
    self.assertEquals(3, linkedlist.head.next.value)
    linkedlist.clear()
  
if __name__ == '__main__':
    unittest.main()
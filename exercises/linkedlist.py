class LinkedList:
  
  def __init__(self):
    self.head = None
    
  def insert(self, value):
    """
    Insert new node to end of linked list.
    @param value: Value of the new node
    """
    if self.head == None:
      self.head = Node(value)
    else:
      nodeptr = self.head
      while nodeptr.next != None:
        nodeptr = nodeptr.next
      nodeptr.next = Node(value)

  def delete(self, value):
    """
    Delete first node from linked list that has matching value.
    @param value: Value of the node to delete
    @return: 0 if no nodes were deleted, 1 if a node was deleted
    """
    if self.head == None:
      return 0
    nodeptr = self.head
    if self.head.value == value:
      self.head = self.head.next
      return 1
    while nodeptr.next != None:
      if nodeptr.next.value == value:
        nodeptr.next = nodeptr.next.next
        return 1
    return 0

  def clear(self):
    """
    Clear all nodes from linked list.
    """
    self.head = None

  def printlist(self):
    nodeptr = self.head
    print nodeptr.value
    while nodeptr.next != None:
      nodeptr = nodeptr.next
      print nodeptr.value

class Node:
  
  def __init__(self, value):
    self.next = None
    self.value = value

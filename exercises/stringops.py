# O(n)
def reverse(string):
  """
  Reverse a string.
  @param string: Input string
  @return: Reversed string
  """
  result = ''
  for i in range(len(string) - 1, -1, -1):
    result = result + string[i]
  return result

# O(n^2)
#def has_unique_chars(string):
#  """
#  Determine if string has all unique characters.
#  @param string: Input string
#  @return: True if string has all unique characters, otherwise False
#  """
#  for i in range(0, len(string) - 1, 1):
#    for j in range(i + 1, len(string), 1):
#      if string[i] == string[j]:
#        return False
#  return True

# O(n)
def has_unique_chars(string):
  """
  Determine if string has all unique characters.
  @param string: Input string
  @return: True if string has all unique characters, else False
  """
  dictionary = {}
  for i in range(0, len(string), 1):
    if string[i] in dictionary:
      return False
    else:
      dictionary[string[i]] = 1
  return True

# O(n)
def is_substring(string1, string2):
  """
  Determine if string1 is a substring of string2.
  @param string1: Input substring
  @param string2: Input string
  @return: True if string1 is a substring of string2, else False
  """
  difference = len(string2) - len(string1)
  if difference < 0:
    return False
  for i in range(0, difference + 1, 1):
    substring = string2[i:i+len(string1)]
    #print 'comparing', string1, 'to', substring
    if string1 == substring:
      return True
  return False
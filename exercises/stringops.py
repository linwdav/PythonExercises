def reverse(string):
  result = ''
  for i in range(len(string) - 1, -1, -1):
    result = result + string[i]
  return result

def has_unique_chars(string):
  for i in range(0, len(string) - 1, 1):
    for j in range(i + 1, len(string), 1):
      if string[i] == string[j]:
        return False
  return True
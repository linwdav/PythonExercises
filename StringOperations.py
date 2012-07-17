def reverse(string):
  result = ''
  for i in range(len(string)-1, -1, -1):
    result = result + string[i]
  return result

def has_unique_chars(string):
  result = False
  
  return result;

def main():
  #print reverse('12345')
  print has_unique_chars('hello')

if __name__ == '__main__':
  main()
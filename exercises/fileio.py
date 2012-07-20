def read_from_file(textfile):
  """
  Read lines from file.
  @param textfile: File to read from
  @return: List of strings, one per line
  """
  infile = file(textfile, 'r')
  array = []
  for item in infile:
    array.append(item.rstrip())
  infile.close()
  return array

def write_to_file(textfile, string_list):
  """
  Write lines to file.
  @param textfile: File to write into
  @param string_list: List of strings to write 
  """
  outfile = file(textfile, 'w')
  for item in string_list:
    outfile.write("%s\n" % item)
  outfile.close()
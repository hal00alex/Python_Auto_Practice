import os
import sys
def one():
  print "Creating file of one type\n"

def two():
  print "Creating file of two type\n"

def three():
  print "Creating file of three type\n"

def main():
  print "Hello Master!\n"
  #get file type from user
  fileType = str(sys.argv[1])
  if (fileType == "-1"):
    one()
  elif (fileType == "-2"):
    two()
  elif (fileType == "-3"):
    three()
  elif (fileType == "-help"):
    print "Please run program with -1, -2, or -3\n"
  else:
    print "Invalid File Type Request"
  print "Goodbye Master\n"
main()

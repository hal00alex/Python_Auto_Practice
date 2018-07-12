def main():
  print "Hello Master\n"
  address = 0x0
  next_address = 0x0
  add_arr = []
  #change for your needs
  y = 20
  inc = 0x1
  for i in range (0, y):
    #may need to change 0x1 to a different number
    next_address = next_address + inc
    add_arr.append(hex(next_address))
  print (hex(next_address))
  #can print array, or one item out of array, or send array to file
  print "\nGoodbye Master\n"
main()

# Data can be output to text file using a file object

f = open("myfile.txt", 'w')     # open file for output 
f.write("First line.\nSecond line.\n")  # write two lines of text
f.close()   # close the file

f = open("myfile.txt", 'a')     # open file for output in append mode
f.write("Third line.\nFourth line.\n")  # write two lines of text
f.close()   # close the file


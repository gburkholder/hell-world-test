print "Hello World!  What's up?"

f_out = open("output.txt", "w+")
f_in = open ("input.csv", "r")

print "File open sucessful"

from subroutine import square_csv

square_csv(f_in, f_out)

f_out.close()
f_in.close()

print "File close sucessful"

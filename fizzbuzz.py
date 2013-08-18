'''
Created on Aug 17, 2013

@author: ramberg
A program that prints the numbers from 1 to 100. 
But for multiples of three print "Fizz" instead of the number 
and for the multiples of five print "Buzz". For numbers which are multiples 
of both three and five print "FizzBuzz".
'''
def main():
    out=""
    for i in range (1,101):
        if (i%3==0):
            out="fizz"
        if (i%5==0):
            out=out+"buzz"
        if (out):
            print out
            out=""
        else:
            print "Number is ",i, ":  Not divisible by 3 or 5"
        
if __name__ == '__main__':
    main()
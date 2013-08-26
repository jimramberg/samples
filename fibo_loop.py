#!/usr/local/bin/python
'''
Created on Aug 26, 2013

@author: ramberg
A looping  function to 
compute the nth Fibonacci number 

'''
def fibonacci(n):
    l1,l2=1,0
    for _ in xrange (0,n+1):
        fibo=l1+l2
        l2,l1=l1,fibo
    return fibo
def main ():
    for i in range(0, 101):
        result = fibonacci(i)
        print "Fibonacci number: ", i, "Value: ", result
if __name__ == '__main__':
    main()

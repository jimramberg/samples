#!/usr/local/bin/python
'''
Created on Aug 25, 2013

@author: ramberg
A recursive function to 
compute the nth Fibonacci number
Added a lookup table ( memoization) to improve performance 

'''
def fibonacci(n):

    if n in (0, 1):
        result=n
        return result
    if n - 2 in fibo.keys():
        el=fibo[n - 2]
    else:
        el = fibonacci(n - 2)   
    if n - 1 in fibo.keys():
        l=fibo[n - 1]
    else:
        l = fibonacci(n - 1)
    result = l + el 
    if n not in fibo.keys():
        fibo[n] = result
    return result
def main ():
    global fibo
    fibo = {
          0:0,
          1:1
          }
    for i in range(0, 101):
        result = fibonacci(i)
        print "Fibonacci number: ", i, "Value: ", result
if __name__ == '__main__':
    main()

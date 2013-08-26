#!/usr/local/bin/python
'''
Created on Aug 25, 2013

@author: ramberg
A recursive function to 
compute the nth Fibonacci number
Added in an additional function to track number of calls 

'''
def fibonacci(n, count):
    result = []
    l = []
    el = []
    if n in (0, 1):
        result.append(n)
        result.append(1)
        return result
    el.append(count)
    el = fibonacci(n - 2, count + 1)   
    l.append(count)
    l = fibonacci(n - 1, count + 1)
    value = l[0] + el[0] 
    result.append(value)
    count = result.append(l[1] + el[1])
    return result
def main ():
    global fibo
    fibo = {
          0:0,
          1:1
          }
    result = []
    for i in range(0, 31):
        result = fibonacci(i, 0)
        print "Fibonacci number: ", i, "Value: ", result[0], "function calls: ", result[1]
if __name__ == '__main__':
    main()

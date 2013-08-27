#!/usr/local/bin/python
'''
Created on Aug 25, 2013

@author: ramberg
A program to time three different ways of computing a fibonacci number

'''
def fibonacci_memo(n):
    if n in (0, 1):
        result=n
        return result
    if n - 2 in fibo.keys():
        el=fibo[n - 2]
    else:
        el = fibonacci_memo(n - 2)   
    if n - 1 in fibo.keys():
        l=fibo[n - 1]
    else:
        l = fibonacci_memo(n - 1)
    result = l + el 
    if n not in fibo.keys():
        fibo[n] = result
    return result
def fibonacci_basic(n):
    if n in (0, 1):
        return n
    el = fibonacci_basic(n - 2)   
    l = fibonacci_basic(n - 1)
    result = l + el
    return result
def fibonacci_loop(n):
    l1,l2=1,0
    for _ in xrange (0,n+1):
        result=l1+l2
        l2,l1=l1,result
    return result
def main ():
    from timeit import Timer
    global fibo
    fibo = {
          0:0,
          1:1
          }
    executions=100
    variations=["fibonacci_basic"," fibonacci_memo"," fibonacci_loop"]
    for i in range(20, 26):
        result = fibonacci_memo(i)
        print "Fibonacci number: ", i, "Value: ", result, ":Time for ",executions," executions\n"
        for vers in variations:
            fibo_call=vers+"("+str(i)+")"
            setup_call="from __main__ import " + vers
            time_value=Timer(fibo_call,setup_call).timeit(executions)
            print vers,  time_value
        print "\n"
if __name__ == '__main__':
    main()

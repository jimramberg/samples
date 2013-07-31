#!/usr/bin/python
sum=2
prev1=2
prev2=1
fib=0
limit=4000000
while (fib<= limit):
 fib=prev1 + prev2
 mod2= fib%2
 if ( mod2 == 0):
    sum= sum + fib
    print fib, " is a multiple of 2: sum is", sum 
 prev2= prev1
 prev1= fib

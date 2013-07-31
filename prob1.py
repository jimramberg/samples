#!/usr/bin/python
sum = 0
for i in range(1,1000): 
 mod3= i%3;
 mod5= i%5;
 if mod3 == 0  or  mod5 == 0:
  sum=sum + i;
  print i, "is a multiple of 3. Sum is ", sum


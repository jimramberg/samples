'''
Created on Sep 2, 2013

@author: ramberg
Takes two integers and adds them without use of a + 
Via binary operations

'''

def bin_add(numberOne, numberTwo,carry):
    number1=numberOne[-1]
    number2=numberTwo[-1]
    if ( carry == '0'):   #  c 0
        if (number1==number2): #  00 or 11
            if (number2 == '0'):# 0 0 c  0
                value='00'
            else: # 1 1 c  0
                value='10'
        else: # 01 or 10
                value='01'  
    else:    # Carry =1 
        if (number1 ==number2):  # 00 or 11 c 1 
            if (number1 == '0'):# 0 0 c  1
                value='01'
            else: # 1 1 c  1
                value='11'
        else: # 01 or 10
            value='10'       
    newOne=numberOne[:-1]
    newTwo=numberTwo[:-1]
    carry=value[0]
    if (newOne!='0b')  and  (newTwo!='0b'):
        value = bin_add(newOne,newTwo,carry) + str(value[-1])
    if ( carry =='1'):
        if (newOne=='0b')  and  (newTwo=='0b'):
            value='0b'+carry+value[1]
        if (newOne=='0b') :
            value = bin_add('0b'+carry,newTwo,'0') + str(value[-1])
        if (newTwo=='0b'):
            value = bin_add(newOne,'0b'+carry,'0') + str(value[-1]) 
    else: 
        if (newOne=='0b') : 
            value = newTwo + str(value[-1])
        if (newTwo=='0b') : 
            value = newOne + str(value[-1])
    return value
def main ():
    start1=9122
    start2=39
    carry ='0'
    number1=bin(start1)
    number2=bin(start2)
    print "Start number one",start1,bin(start1),"number two",start2,bin(start2)

    final=bin_add(number1,number2,carry)
    print "sum is: ", final, " Which is ",int(final,2),start1+start2
if __name__ == '__main__':
    main()
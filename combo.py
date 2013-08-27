'''
Created on Aug 26, 2013

@author: ramberg
A routine to print out all the possible letter combinations to a seven digit phone number
'''
def build_combo(loop,level,combo):
    newcombo=[]
    for letter in loop[level]:
        for charlist in combo:
            newcombo.append(charlist+letter)
    level +=1
    if (level < 7):
        combo=newcombo
        newcombo=build_combo(loop,level,combo)
    return newcombo
def main():
    keypad={'0':'0' ,
            '1':'1' ,
            '2':'ABC' ,
            '3':'DEF' ,
            '4':'GHI' ,
            '5':'JKL' ,
            '6':'MNO' ,
            '7':'PQRS',
            '8':'TUV' ,
            '9':'WXYZ'}
    loop=[]
    phonenumber='8645328'
    for number in phonenumber:
        loop.append(keypad[number])
    combo=loop[0]
    newcombo=build_combo(loop,1,combo)
    i=1
    for values in newcombo:
        print i,values
        i +=1
if __name__ == '__main__':
        main()
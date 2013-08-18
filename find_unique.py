'''
Created on Aug 18, 2013

@author: ramberg
Find non repeated alphabetical characters in a file 
'''
def main():
    charcount=dict()
    myfile="/var/log/system.log"
    f=open(myfile,"r")
    for line in f.readlines():
        for c in line:
            if c.isalpha():
                if c in charcount:
                    charcount[c]+=1
                else:
                    charcount[c]=1
    for key in charcount:
        if (charcount[key]==1):
            print key , "is non repeated"
        else :
            print key ,"has value:", charcount[key]
if __name__ == '__main__':
    pass
main()
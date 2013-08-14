'''
Created on Aug 14, 2013

@author: Jim Ramberg
a smarter way to read to parse a large log file '''
import re
mylist=[]
mylogfile="/var/log/system.log" #any log to check
searchterm="Anchors" # any term you want
offset=15 # to edit out time and date if needed
f=open(mylogfile)
for line in f:
    if re.search(r"Anchors",line): 
        foo=line[15::]
        myhash=hash(foo)
        if myhash not in mylist:
            mylist.append(myhash)
            print foo

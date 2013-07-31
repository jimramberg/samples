#!/usr/bin/python

def openlog():
# logname: system log file to read from. OS dependant
    logname = "/var/log/system.log"
    try:
        f = open(logname, 'r')
    except IOError:
        print " Can't find file %s for reading" % logname
        exit(1)
    return f
def main ():
# offset : this is the amount of column offset for the log file .  OS dependant
    offset = 4  
    logfile = {}
    f=openlog()
# main loop that will parse the entire file 
    for line in f: 
# Split the readin line into a  list. 
        w = line.split(' ') 
# Create a new line; minus the filtered out lines from the offset 
        a = ' '.join(w[offset:]) 
# Check to see if the line already exists as a key
        if logfile.has_key (a): 
            logfile[a] += 1 
# Create new key with value set to one 
        else:  
            logfile[a] = 1
            
            
# Now we need to sort and parse the dict
    keys = logfile.keys()
    keys.sort()
    values = logfile.values()
# Find the top 9 values
    top = sorted(values, reverse=True)[0:9]
    dashedline=79*'-'
    print  " Results"            
    for t in top:
        print dashedline
        print " Shows up %s times " % t
        print dashedline
        for m in logfile:
            if logfile[m] == t:
                print "Line:  %s" % m 
    f.close()
                
if __name__ == '__main__':
    main()
                    
    
    

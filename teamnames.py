#!/usr/bin/python
def make_name(names,letters):
    namelength = len(names)
    letterlength = len(letters)
    for i in range (0,namelength):
        index = i%letterlength 
        team = names[i]+'_'+letters[index]
        print " Name is %s " % team

def main ():
    Names  = ['team1','team2','team3','team4','team5','team6']
    Letters = ['A','B','C']
    make_name(Names,Letters)
if __name__ == '__main__':
    main()
                    
  

'''
Author: Jim Ramberg: 18-August-2013

Problem:  You are given a list of team names} ['team1','team2','team3','team4','team5','team6']

Write a program that will add a suffix consisting of an underscore and a letter (A,B,C). The letters must follow sequential order. Once 'C" is used; go back and repeat the process. Your output should look like:

 Name is team1_A 
 Name is team2_B 
 Name is team3_C 
 Name is team4_A 
 Name is team5_B 
 Name is team6_C 
 '''
#!/usr/bin/python
def main ():
    Names  = ['team1','team2','team3','team4','team5','team6']
    Letters = ['A','B','C']
    for teamname in Names:
        suffix=Letters.pop(0)  #pop the first suffix letter
        newname=teamname+"_"+suffix
        print newname
        Letters.append(suffix) # now put it at the end of the list 
if __name__ == '__main__':
    main()
                    
  

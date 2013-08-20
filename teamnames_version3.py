'''
Created on Aug 19, 2013
Problem:  You are given a list of team names} ['team1','team2','team3','team4','team5','team6']

Write a program that will add a suffix consisting of an underscore and a letter (A,B,C). The letters must follow sequential order. Once 'C" is used; go back and repeat the process. Your output should look like:

 Name is team1_A 
 Name is team2_B 
 Name is team3_C 
 Name is team4_A 
 Name is team5_B 
 Name is team6_C 


Original author:Bradford Chin <bchin@clustrix.com>
filled out by  ramberg
'''
def main():
    print " Now running method 1"
    method_1()
    print " Now running method 2"
    foo=method_2()
    for i in foo:
        print i
def method_1():
    new_array=[]
    names= ['team1','team2','team3','team4','team5','team6']
    teams= ['A','B','C']
    for i,n in enumerate(names):
        new_array.append('%s_%s' %(n, teams[i % len(teams)]))
    for newname in new_array:
        print newname
def method_2():
    names= ['team1','team2','team3','team4','team5','team6']
    teams= ['A','B','C']
    ln = len(names)
    teamext = ln/len(teams) + 1
    largerteam= teams * teamext
    diff = len(largerteam)-ln
    
    return map(lambda n, t: "%s_%s" % (n,t), names, largerteam)[:-diff]

if __name__ == '__main__':
    main()
# Program to calculate longest word in a List

def longestWords (name):  
    stringsLen = []
    for i in name:
        if type(i) == str:
            stringsLen.append(len(i))
    print max(stringsLen)     
  
#calling the function   
longestWords(['Sachin','Rohit','Anjali', 'Ajitesh'])   

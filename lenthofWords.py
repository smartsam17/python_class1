# Length of words in a list
def longestWords (name):  
    stringsLen = []
    for i in name:
        if type(i) == str:
            stringsLen.append(len(i))
    print stringsLen   
  
#calling the function   
longestWords(['Sachin','Rohit','Anjali', 'Ajitesh'])   

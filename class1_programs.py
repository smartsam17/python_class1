#print as comma sequece in a single line,divisble by 7 but not a multiple of 5 in between 2000 and 3200,

numbers = [];
for i in range(2000, 3201):
    if i%7 == 0 and i%5 != 0 :
        numbers.append(str(i))
print (",".join(numbers))



# Print the first name and last name in reverse order

def reverstring(name):
    return name[::-1]

reversName =  reverstring('Sachin Gupta')  
print(reversName)


#volume of sphere with diameter 12

pi=22/7
radius = 12/2
volume = (4 / 3) * pi * radius * radius * radius
print("Volume is: ", volume)

# take a comma separated number and genarate the list
inp = '1,2,3,4,5,6'
separator = ','
formattedInput = inp.split (",")
listFianl = []
for i in formattedInput:
        listFianl.append(int(i))
print(listFianl)   

#/////////////////////////////////////

limit = 9
for i in range(0,limit):
        print ('\n')
        
        if i > limit/2:
            j = limit-i-1
            i = j
        for j in range(0,i+1):
            print('*' ,end=' ')
            
#////////////////////////////////////
print('WE, THE PEOPLE OF INDIA,\n\t having solemnly resolved to constitute India into a SOVEREIGN,! \n\t\t SOCIALIST SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens')
            
            



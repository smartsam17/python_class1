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

#print as comma sequece in a single line,divisble by 7 but not a multiple of 5 in between 2000 and 3200,

numbers = [];
for i in range(2000, 3201):
    if i%7 == 0 and i%5 != 0 :
        numbers.append(str(i))
print (",".join(numbers))

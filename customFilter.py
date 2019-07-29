filterList = [12,4,13]
ageFilterList = []
def customFilter(myfunc,filterList):
  for listItem in filterList:
    if myfunc(listItem):
      ageFilterList.append(listItem)
  return ageFilterList     

def myfunc(listItem):
   if listItem > 10:
     return True

y = customFilter(myfunc,filterList)
print (y)

          


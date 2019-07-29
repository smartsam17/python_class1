from functools import reduce # only in Python 3
def do_sum(x1, x2): 
  print (x1)
  print (x2)
  return x1 + x2
print(reduce(do_sum, [1, 2, 3, 4]))


itemList = [1,8,10,12]
def reduce_custom(myfunc, itemList):
  return myfunc(itemList)

def myfunc(itemList):
  sumItems = 0
  for item in itemList:
    sumItems += item 
  return sumItems    

sumOfNumbers = reduce_custom(myfunc, itemList)
print (sumOfNumbers)


from functools import reduce

mojaLista = [1,2,3,4,5,6,6,4,3,23,2]
newList = [x ** 2 for x in mojaLista if x % 2 ==0] #listy składane
print(newList)

# map() filter() reduce()

newList1 = list(map(lambda x: x*2, mojaLista))
print(newList1)

newList2 = list(filter(lambda x: x% 2 ==0,mojaLista))
print(newList2)

newList3 = reduce(lambda x, y: x+y,mojaLista)
print(newList3)

a= 2
b=3
input = "2+2 - a*b"
# input = "2+2-56+125"
output = eval(input)
print(output)

inputDate ="""
mojaLista = [1,2,3,4,5,6,6,4,3,23,2]
newList = [x ** 2 for x in mojaLista if x % 2 ==0] #listy składane
print(newList)
"""

exec(inputDate)
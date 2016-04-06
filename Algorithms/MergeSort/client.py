from mergeSort import *

#items = [27, 85, 8, 19, 98, 5, 78, 21, 35, 96, 78, 1,
#         90, 100, 193, 104, 18, 8540, 84, 59,65,15,78,
#         42,7,184,963,852,745,145]
items = [8,20,1,19,60,0]
print("Starting Merge Sort Algorithm")
obj = mergeSort()
obj.sort(items)
items = obj.getItems()

print("Sorted List: ", items)

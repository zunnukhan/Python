import array as arr
array_num=arr.array('i',[1,5,3,7,4,3])
print("Original array: "+str(array_num))
print("Number of occurrences of the num 3 in the said array: "+str(array_num.count(3)))
array_num.reverse()
print("Reverse the order of the items: ")
print(str(array_num))
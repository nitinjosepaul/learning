list1 = [1,2,3,4,5,6,7]
list_len = len(list1)
for index in range(0,list_len,2):
    try:
        temp = list1[index]
        list1[index] = list1[index+1]
        list1[index+1] = temp
    except IndexError:
        print("The list has odd number of elements!")
print(list1)

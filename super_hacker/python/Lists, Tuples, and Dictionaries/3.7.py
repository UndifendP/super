num_list =[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
undublicated_list = []
for i in num_list:
    if i not in undublicated_list:
        undublicated_list.append(i)
print(undublicated_list)

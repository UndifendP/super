rand_num_list =[10, 1, 8, 3, 5,20, 33,11]
backup_list =[]
backup_list=rand_num_list.copy()
sorted_num_list =[]
for i in range(len(rand_num_list)):
    sorted_num_list.append(min(rand_num_list))
    rand_num_list.remove(min(rand_num_list))
print(sorted_num_list)
#print(backup_list)

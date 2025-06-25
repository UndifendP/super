num_list =[1,2,3,4,5,6,7,8,9,10,1]
text=''
st_list =[]

st_list=str(num_list)
for i in st_list:
    if i ==',' or i=='['or i==']':
        continue
    elif i == ' ':
        text+=','
    else:
        text+=i
# final=re.sub(r'',',',text)
print(text)

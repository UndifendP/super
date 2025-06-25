text=input("Enter text:")
for i in text:
  counter=0
  if i!=" ":
   for j in text:
      if i==j:
        counter+=1
  if i!=" ":
    print(i,counter)

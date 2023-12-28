myTuple=(4, 5, 4, 5, 6, 6, 5, 5, 4)
my_dictionary={}
for i in myTuple:
 print(i)
 
for i in myTuple:
 if i in my_dictionary:
  my_dictionary[i]=my_dictionary[i]+1
 else:
  my_dictionary[i]=1
print("Tuple=" ,myTuple)  
print("Dictionary= ",my_dictionary)


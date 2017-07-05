print("Programme for finding average of numbers")
sum=0
i=1
count=0
while(1):
    ch=input("\nDo you wish to add a number ")
    if(ch=='y'):
      a=input("\nEnter your number")
      a=int(a)
      sum=sum+a
      count=count+1
      i=i+1
    else:
      break
average=sum/count
print("\nThe average of the numbers is:")
print(average)
 

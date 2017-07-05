print("Program to print ASCII code")
message=input("\nEnter the message ")
print("\nThe ASCII code is : ",end=' ')
for ch in message:
  print(ord(ch),end=' ')


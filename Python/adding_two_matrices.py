a=[]
print("List 1: ")
choice=int(input("Enter an integer. To stop,enter 0: "))
a.append(choice)
while(choice!=0):
    choice=int(input("Enter an integer. To stop,enter 0: "))
    a.append(choice)
a.remove(0)
print("List 1 Created")

print("\nList 2: ")
b=[]
choice=int(input("Enter an integer. To stop,enter 0: "))
b.append(choice)
while(choice!=0):
    choice=int(input("Enter an integer. To stop,enter 0: "))
    b.append(choice)
b.remove(0)
print("List 2 Created")

if(len(a)!=len(b)):
   print("\nBoth matrices should have equal entries!!!")

l=len(a)
i=0
while(i<l):
    a[i]=a[i]+b[i]
    i=i+1
print("\nThe sum of the two matrices is: ")
print(a)
    

    
    

    
    
        
    
    

    
        
        

    
         
   


    
        
        

    


        
    
        
    

    
    


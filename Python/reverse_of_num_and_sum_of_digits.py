num=input("Enter a number: ")
c=input("Enter 1 for reversed number and 2 for sum of digits: ")
if(c=='1'):
    l=len(num)
    num=int(num)
    b=str(num%10)
    num=num//10
    i=1
    while(i<l):
        a=num%10
        num=num//10
        b=b+str(a)
        i=i+1
    print("\nThe reverse is: ",b)
    print("\nThank You")
elif(c=='2'):
    sum=0
    for i in num:
        i=int(i)
        sum=sum+i
    print(sum,'\nThank You')
else:
    print("\nWrong Entry!!!")
    

    

    

    
    

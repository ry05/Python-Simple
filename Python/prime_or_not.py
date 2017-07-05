n=int(input('Enter the number: '))
i=2
cnt=0
while(i<n):
    if(n%i==0):
        cnt=cnt+1
        break
    else:
        cnt=0
    i=i+1
if(cnt==0):
    print('Prime')
else:
    print('Composite')



        
    

    
        
        
        
    



print('Bank Management System')
b=[]
c='y'
while(c=='y'):            
        name=input('Enter customer name: ')
        accno=str(input('Enter the account number: '))
        amount=int(input('Enter the amount you have: '))
        b.append((accno,(name,amount)))
        c=input('do u want to enter details? ')
bank=dict(b)
print(bank)
def update_1():
    ch=input('Do u wish to update any account? ')
    if(ch=='y'):
        key=input('Enter the account number: ')
        update_2(key)
    else:
        print('Thank You')
def update_2(k):
    accnos=str(list(bank.keys()))
    for i in accnos:
        if(i==k):
            bank[i]=(str(input('Enter the name : ')),int(input('Enter the revised amount : ')))
    print(bank)
update_1()
    
    
    
    
    
        

    
    
        
    
    

    
        
        

    
         
   


    
        
        

    


        
    
        
    

    
    


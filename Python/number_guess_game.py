import random
n=random.randint(1,100)
pts=100
c=1
i=1
print("Hello Player! Welcome to the Number Guess Game!\n U get like 10 chances to guess a number that the computer generates...\n You have clues but only at try 1,try 4 and try 7. \n WARNING: YOU LOSE POINTS FOR EACH CLUE!")
while(i<=10):
     a=int(input("\nEnter number between 1 and 100: "))
     if(a==n):
         print("\nYou win!")
         c=0
         break
     elif(a<n):
         print("\nNumber is larger ")
         clue=input("Do you want a clue?")
     elif(a>n):
         print("\nNumber is smaller ")
         clue=input("Do you want a clue?")
     if(i==1):
        if(clue=='yes'):
             print("\nClue 1 is that number is between ",n-10," and ",n+14)
             pts=pts-10
        else:
            print("Continue\n")
         
     elif(i==4):
        if(clue=='yes'):
             print("\nClue 2 is that number is between ",n-2," and ",n+5)
             pts=pts-25
        else:
            print("Continue\n")

     elif(i==7):
        if(clue=='yes'):
             print("\nClue 3 is that number is between ",n-2," and ",n+9)
             pts=pts-40
        else:
            print("Continue\n")

     elif(i==2):
          if(clue=='yes'):
            print("\nNo clue available")
            print("Continue\n")
     elif(i==3):
          if(clue=='yes'):
            print("\nNo clue available")
            print("Continue\n")
     elif(i==5):
          if(clue=='yes'):
            print("\nNo clue available")
            print("Continue\n")
     elif(i==6):
          if(clue=='yes'):
            print("\nNo clue available")
            print("Continue\n")
     elif(i==8):
          if(clue=='yes'):
             print("\nNo clue available")
             print("Continue\n")
     elif(i==9):
          if(clue=='yes'):
            print("\nNo clue available")
            print("Continue\n")
     elif(i==10):
          if(clue=='yes'):
            print("\nThis was your last chance!How must I provide you a clue??")
     i=i+1
if(c==1):
    print("\nYou lose,Better luck next time")
else:
    print("\nPoints you have scored is: ",pts)
    



     
    


    

    

    
    

import random
print("Enter your choice \n  - Rock \n  - Paper \n  - Scissors \n")
player1 =input("enter target :").capitalize()
print("System is being selected")
list1=["Rock","Paper","Scissors"]
player2=random.choice(list1)
print("system :",player2)
if player1==player2:
    print("no winner")
 
elif player1== "Rock" and player2=="Paper":
    print("The computer won")
elif player1== "Rock" and player2=="Scissors":
    print("The player won")
    
elif player1== "Paper" and player2=="Rock":
     print("The player won")
     
elif player1== "Paper" and player2=="Scissors":
      print("The computer won")
      
          
elif player1== "Scissors" and player2=="Paper":
      print("The computer won")
              
elif player1== "Scissors" and player2=="Rock":
      print("The computer won")
                    
import random
import time


name= input("Please enter your name: ")

def playAgain():
     userInput=input("Would you like to play again? Y/N: ")
     done = False
     while not done:
          if userInput !='y' and userInput != 'Y':
               print("Goodbye")
               done = True
          else:
               done = False
               gamePlay()
               
     
                
def gameRules():
     #print(time.asctime())
     print("Welcome to the BlackJack game.")
     print("Game rules:")
     time.sleep(1)
     print("You need to make 21 to win BlackJack")
     print("You enter the first number and the computer picks the second")
     print("The computer picks a random number between 5 and 14")
     time.sleep(2)
     print("If the two numbers add up to 21 then you won the BlackJack. ")
     input("Hit Enter/Return to start: ")
     time.sleep(1)
     gamePlay()
     
     
     
def gamePlay():
     total_sum = 0
     a = int(input("Enter your first number: "))
     b = random.randint(5,14)
     print("The computer picks", b)
     while (a +b) != 0:
         total_sum = a+b
         time.sleep(1)
         if total_sum >21:
             print('Total sum is', total_sum)
             print("You lost")
             time.sleep(1)
             playAgain()
             break
         elif total_sum<21:
             print("Your total sum is", total_sum)
             playAgain()
             break
         elif total_sum==21:
             print("BLACKJACK!)
             time.sleep(1)
             for i in range(total_sum):
                  total_sum=total_sum-1
                  time.sleep(0.3)
                  print(total_sum)
                  print(name, "you are a winner!")
             playAgain()
             break


gameRules()

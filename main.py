#the pupose of this program is to ask to questions 
import random

def main():
    run_program = "y"
    #defining run_program as "y" to enter the while loop.
    while run_program == "y" or run_program == "Y":
      intro()
      run_the_thing()
        #calls the program converting all the shit


      run_program = input("run program?")


#ask if the user wants to play the program again
def intro():
    print("Divide by 9, 10 questions:")  #this needs to be inside 3 double quotes it will give an error on the python shell
    print("--" * 17)
    print("You will be...... ")#more detail

    #intro  
def run_the_thing():
  #print("hello")
  score = 0
  num = list(range(1,13,1))
  random.shuffle(num)
  #print(num)
  for i in range(10):
    num1 = num[i]
    num2 = 9
    num3 = num1*num2
    pick = random.randrange(3)
    if pick == 0:
        print(f"{num3} \u00f7 {num2} = ____",end="\t") 
        answer = int(input("Answer: "))
        correct = num1
    elif pick == 1:
        print(f"____ \u00f7 {num2} = {num1}",end="\t") 
        answer = int(input("Answer: "))
        correct = num3
    else:
        print(f"{num3} \u00f7 ____ = {num1}",end="\t") 
        answer = int(input("Answer: "))
        correct = num2  	

    if answer == correct:
        score += 1
        print("correct")
    else:
        print(f"Good try, but the correct answer is {correct}")
  print(f"This is your {score}")
		#makes scores (setup nothing before the for loop and then when correct print score)
main()


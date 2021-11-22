#the pupose of this program is to convert amounts from the metric system to the US measring system
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
    print(
        "Divide by 9 questions"
    )  #this needs to be inside 3 double quotes it will give an error on the python shell


    #intro  print("--" * 17)
def run_the_thing():
  print("hello")
num = list(range(1,13,1))

random.shuffle(num)
print(num)
for i in range(10):
	num1 = num[i]
	num2 = 9
	num3 = num1*num2
	print(f"{num1} \u00f7 {num2} = ____",end="\t") 
	answer = int(input("Answer: "))



main()

print("Goodbye!")

#$$$ so for each of your A B and C you are getting the first number and then doing 2 calculations to convert it to the other 2 units, then print all three (the one typed in and the 2 calculated/converted)
#!!!! I don't get it what you mean, sorry but the code loops now :)

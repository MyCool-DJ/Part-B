#the purpose of this program is to ask 10 questions for the user to practice their math questions, in this program it's divided by 9.
import random  #this imports a random number function in python.


def main(
):  #this is the main function for the entire program and always asks the user to run the program again or if they want or to exit.
    run_program = "y"  #this stores the variable of run_program with a value of y as a string.
    #defining run_program as "y" to enter the while loop.
    while run_program == "y" or run_program == "Y":  #a while loop that checks if run_program is equal to y or Y and if so it runs the functions intro and runs the thing by calling them inside the while loop.
        intro()  #calls the intro function
        run_the_thing()  #calls the run_the_thing function
        run_program = input(
            "run program?"
        )  #stores the value of the string to check in our while loop to decide to run_the_thing


def intro(
):  #this function controls the intro function, it loads the information for the user to be able to understand what the program does in the console, it also displays every time the program runs.
    print(" \t \t MATH QUESTIONS ")  #tells the user the title of the program
    program = (
        "dividing by 9"  #tells the user what the program does
    )
    print("--" *
          20)  # to break up in the console the text, makes it easier to read
    print(
        f"You will be asked 10 questions based on:\n{program}"
    )  # This tells the user how many questions to expect as only one will load at a time
    print("--" * 20)


def run_the_thing():  #this is the function that holds the guts of the program
    print("Please try your best to answer, you got this!"
          )  #postive encouragement helps the user try
    score = 0  #this stores the default value of the score variable as zero.
    num = list(range(1, 13, 1)) #this variable creates a list in a range of a start of 1 a stop of 13, and a step of 1
    random.shuffle(num) #this command uses our imported random at the beginning of our code then shuffles the num list
    for i in range(10): #our for loop that uses I as the counting variable in range 10 which means our code block loops 10 times before exiting
        num1 = num[i] #holds the value of the counter variable and the num list
        num2 = 9 #this program is divided by the integer 9 so the value stored is the number 9
        num3 = num1 * num2 # as we are dividing by we need to times the list value by the number 9, before we can divide by 9
        pick = random.randrange(3) # we want to mix it up the different ways the questions can ask the calculations for our users and to then have them fill in the blank! We do this with a randrange with 3 as the parameter in the parenthesis.
        if pick == 0: 
            print(f"{num3} \u00f7 {num2} = ____", end="\t")
            answer = int(input("Answer: "))
            correct = num1
        elif pick == 1:
            print(f"____ \u00f7 {num2} = {num1}", end="\t")
            answer = int(input("Answer: "))
            correct = num3
        else:
            print(f"{num3} \u00f7 ____ = {num1}", end="\t")
            answer = int(input("Answer: "))
            correct = num2

        if answer == correct:
            score += 1
            print("correct")
        else:
            print(f"Good try, but the correct answer is {correct}")
    print(f"This is your score {score}")


#makes scores
main(
)  #calls the main function this is needed for the program to fun it controls all the functions inside the main function

print(
    "Thanks for playing"
)  #if the user decides to exit the program they will get a goodby statement as a confirmation

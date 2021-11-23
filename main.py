#the pupose of this program is to ask 10 questions for the user to practice their math questions, in this program divided by 9
import random  #this imports a random number funtion in python


def main(
):  #this is the main function for the entire program and always the user to run the program again if they want or to exit.
    run_program = "y"
    #defining run_program as "y" to enter the while loop.
    while run_program == "y" or run_program == "Y":
        intro()
        run_the_thing()
        #calls the program converting all the shit

        run_program = input("run program?")


#ask if the user wants to play the program again
def intro(
):  #this funtion controls the intro funtion it loads the information for the user to be able to understand what the program does in the console
    print(
        "Divide by 9"
    )  #this needs to be inside 3 double quotes it will give an error on the python shell
    program = (
        "dividing by 9"
    )  #I add this as if this code was extended I was thinking different programs could use this title so a varible to say what program this is, made sense to me
    print("--" * 17)  # to break up in the console the text
    print(f"You will be asked 10 questions based on:\n{program}")  #
    print("--" * 17)


def run_the_thing():
    print("Loading...")
    score = 0
    num = list(range(1, 13, 1))
    random.shuffle(num)
    #print(num)
    for i in range(10):
        num1 = num[i]
        num2 = 9
        num3 = num1 * num2
        pick = random.randrange(3)
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
)  #calls the main funtion this is need for the program to fun it controls all the functions inside the main funtion

print(
    "Thanks for playing"
)  #if the user decides to exit the program they will get a goodby statement as a conformation

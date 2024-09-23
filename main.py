from trivia import *
import random 

def main():
    rand = random.Random()
    answers = [] 
    questions = []
    score = 0
    
    for num in range(len(trivia)): #for how ever many questions there are, make a list of all the indexes
        questions.append(num)
    #print(questions)
    

    loop = range(len(trivia))
    for num in loop:
        ques = rand.randrange(len(questions)) #select index of a random question in questions
        print(ques)
        ask_question(trivia[questions[ques]])
        answers.append(get_inp())  
        print(answers)

        questions.remove(questions[ques])#remove the questions index so it doesn't get caled again 
        
    

    
        

def ask_question(question): #print trivia question and answers 
    print(question["question"])
    for option in question["options"]:
        print(option)

        




def get_inp(): #loop until valid input 
    ax = True
    while (ax):
        inp = input("a, b, c, d? \n").lower()
        if (inp == "a" or inp == "b" or inp == "c" or inp == "d" or inp == "e" or inp == "f" or inp == "g" or inp == "h"):
            ax = False
            print(f"you selected {inp}")
            return inp
        else :
            print("invalid answer")



if __name__ == "__main__":
    main()

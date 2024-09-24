from trivia import *
import random 

def main():
    rand = random.Random()
    answers = [] 
    questions = []
    score = 0
    max_score = 0
    
    for num in range(len(trivia)): #for how ever many questions there are, make a list of all the indexes
        questions.append(num)
    #print(questions)
    

    loop = range(len(trivia))
    for num in loop:
        ques = rand.randrange(len(questions)) #select index of a random question in questions
        
        ask_question(trivia[questions[ques]])
        answers.append(get_inp())  
        #print(answers)
        max_score += trivia[questions[ques]]["score"] # always add score for max_score
        if (answers[len(answers) - 1] == trivia[questions[ques]]["answer"]): # if the input == the answer += the score
            score += trivia[questions[ques]]["score"]
            print(trivia[questions[ques]]["correct_output"])
        else :
            print(trivia[questions[ques]]["incorrect_output"])

        
        questions.remove(questions[ques])#remove the questions index so it doesn't get caled again 
        
    print(f"you got a score of {score} out of {max_score} points!\nThanks for Playing!")
    
    
        

def ask_question(question): #print trivia question and answers 
    print(question["question"])
    for option in question["options"]:
        print(option)

def get_inp(): #loop until valid input 
    ax = True
    while (ax):
        inp = input("a, b, c, d? \n").lower()
        if (inp == "a" or inp == "b" or inp == "c" or inp == "d"):
            ax = False
            print(f"you selected {inp}")
            return inp
        else :
            print("invalid answer")



if __name__ == "__main__":
    main()

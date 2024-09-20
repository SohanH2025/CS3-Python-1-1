from trivia import *

def main():
    answers = []
    for num in range(len(trivia)):
        print(trivia[num]["question"])
        for option in trivia[num]["options"]:
            print(option)
        
        answers.append(get_inp())
        print(answers)
        

    
        




def get_inp():
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

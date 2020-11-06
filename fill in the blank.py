#start with game
#below is th eprogram for madlibs game
#this is simple text series question game. This was a grat starter project to have hands on experience 
# with python syntax with array, list, functions, contionals statments and interactibg with input and output from user
print("let's begin the quiz. you will get 5 attempts for answering in the quiz." )
print("Good Luck!")

num_of_blank = ["__1__", "__2__", "__3__", "__4__"] 

easy_question = ("A __1__ is something that holds a __2__, and a __3__ is a list of characters in order.\
    You can also __4__ a string to a variable.")
easy_answers = ["variable", 
 "value", 
 "string", 
 "assign"]

medium_question = ("An example of __1__ is an __2__ statement.  If statements can run at most __3__ time.\
    Unlike the if statement, a __4__ loop can run any number of times.")
medium_answers = ["control flow", 
 "if", 
 "one", 
 "while"]

hard_question = ("A __1__ is when you have a list within a list. Lists support __2__, this means we can\
    change the value of a list after it has been created.  When you have two different ways to refer to the\
    same object that is called __3__.In a __4__ loop, for each element in the list, you will assign that\
    element to the name and evaluate the block.")
hard_answers = ["nested", 
 "mutation", 
 "aliasing", 
 "for"]


'''allows user to select the level and print the selected level question'''
def question_level(difficulty): 
    if difficulty.lower() == 'easy':
        question = easy_question
        print(question)
        answer=easy_answers
        game(question,answer)
    elif difficulty == 'medium':
        question = medium_question
        print(question)
        answer=medium_answers     
        game2(medium_question,medium_answers)
        
    elif difficulty == 'hard':
        question = hard_question
        print(question)
        answer=hard_answers        
        game3(question,answer)
        
    else:
        print("That is not a level.")
'''
def word_in_question(word, some_list): 
    for item in some_list:
        if item in word_to_check:
            return item
    return None
'''

'''display easy question and plays the 
game ahead if the user is giving in correct answer'''
def game(some_string,some_list): 
    for word, answer in zip(num_of_blank, easy_answers):

        while True:
            guess = input("what goes in blank" + word + "?")
            if guess == answer:
                print("correct answer")
                some_string = some_string.replace(word,guess, 5)

                print(some_string)
                break
            else:
                print("wrong answer, try again")
    
    print("awesome!! Completed the level")

''' display medium level question and plays the game
ahead if the user is giving in correct answer'''
def game2(some_string2,some_list): 
    
    for word, value in zip(num_of_blank, medium_answers):

        while True:
            alpha = input("what goes in blank " + word + "?")
            if alpha == value:
                print("correct answer")
                some_string2 = some_string2.replace(word,alpha, 5)

                print(some_string2)
                break
            else:
                print("wrong try again")
                        
    print("awesome!! Completed the level")


'''display hard level question and plays the game 
 ahead if the user is giving in correct answer'''
def game3(some_string3,some_list):

    for word, ans in zip(num_of_blank, hard_answers):

        while True:
            beta = input("what goes in blank" + word + "?")
            if beta == ans:
                print("correct answer")
                some_string3 = some_string3.replace(word,beta, 5)

                print(some_string3)
                break
            else:
                print("wrong try again")
        
    print("awesome!! Completed the level")


difficulty = input("Please select a level of difficulty for your questions: Easy, Medium, or Hard. ")

'''for calling the function and starting with game'''
question_level(difficulty)
















    

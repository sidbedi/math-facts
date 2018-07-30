import random


def ask_problem():

     global score
     operand1 = random.randint(1,12)
     operand2 = random.randint(1,12)
     guess = input('what is ' + str(operand1) + ' + ' + str(operand2) + '? ')
     #change this line to define answer
     #hint answer = 
     answer = operand1 + operand2
     guess=int(guess)
     if guess == answer:
        print('correct answer')
        score = score + 1
     if guess != answer:
        print('wrong answer!')





score = 0
runme=1
print('welcome to math quiz!')
while runme < 10:
     ask_problem()
     runme=runme+1

print('your score is ' + str(score) + "\n")
print('good game!!! :)')



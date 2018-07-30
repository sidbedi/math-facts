def ask_problem():

     global score


     guess = input('what is 2+2? ')

     #change this line to define answer
     #hint answer = 
     answer = '4'

     if guess == answer:

        print('correct answer')

        score = score + 1

     if guess != answer:

        print('wrong answer!')





score = 0

print('welcome to math quiz!')

ask_problem()

print ('good game!!! :)')



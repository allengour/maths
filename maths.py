import random
import datetime

attempts = 0
correct = 0
precision = 0.001

def ask(option, lower=0, upper=20):
    global attempts
    global correct
    x = random.randrange(lower+1, upper+1)
    y = random.randrange(lower+1, upper+1)
    question = '{} * {} = '.format(x,y)
    answer = x * y
    if option == 'fr':
        question = '1/{} = '.format(x)
        answer = round(1/x, 3)
    elif option == 'sq':
        question = '{} * {} = '.format(x,x)
        answer = x*x
    while True:
        attempt = input(question)
        if attempt == 'quit':
            if attempts > 0 and correct > 0:
                print('Ending session...\n\nStats:')
                print('  accuracy: {}%'.format(round(correct/attempts*100, 2)))
                print('  speed: {}s per question'.format(round((datetime.datetime.now()-start).total_seconds()/correct, 2)))
            import sys
            sys.exit()
        try:
            attempts += 1
            if abs(eval(attempt) - answer) < precision:
                print('correct.')
                correct += 1
                break
            else:
                continue
        except:
            print('Please enter a number. Enter \'quit\' to quit.')

def addition(lower, upper):
    global attempts
    global correct
    x = random.randrange(lower+1, upper+1)
    y = random.randrange(lower+1, upper+1)
    question = '{} + {} = '.format(x,y)
    answer = x + y
    while True:
        attempt = input(question)
        if attempt == 'quit':
            if attempts > 0 and correct > 0:
                print('Ending session...\n\nStats:')
                print('  accuracy: {}%'.format(round(correct/attempts*100, 2)))
                print('  speed: {}s per question'.format(round((datetime.datetime.now()-start).total_seconds()/correct, 2)))
            import sys
            sys.exit()
        try:
            attempts += 1
            if eval(attempt) == answer:
                print('correct.')
                correct += 1
                break
            else:
                continue
        except:
            print('Please enter a number. Enter \'quit\' to quit.')

start = datetime.datetime.now()

try:
    option = input('Enter \'fr\' for fractions, \'sq\' for squares, \'mu\' for multiplication, or \'ad\' for addition: ')
    lower = eval(input('Enter lower bound: '))
    upper = eval(input('Enter upper bound: '))
except:
    print('Using default range (0,20)...')
    lower, upper = 0, 20

if option == 'ad':
    while True:
        addition(lower, upper)    

while True:    
    ask(option, lower, upper)
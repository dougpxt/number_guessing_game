import random
import keyboard

def findout_number():
    number = random.randint(1, 100)

    while True:
        guess = int(input('What is the number? Give me a shot: '))

        if keyboard.is_pressed('esc'):
            print('You chose to exit the game')
            return False, number
        if guess == '':
            continue

        # 
        short_lower_limit = number - 12
        short_upper_limit = number + 12
        close_error_margin =  range(short_lower_limit, short_upper_limit + 1)
        
        big_lower_limit = number - 24
        big_upper_limit = number + 24
        far_error_margin = range(big_lower_limit, big_upper_limit + 1)
        # 
        
        if guess == number:
            return True, number
            break
        elif guess != number and guess in close_error_margin:
            print('You are close')
        elif guess != number and guess in far_error_margin:
            print('You are far')
        else:
            print('You are too far')

# 

result, number = findout_number()
if result == True:
    print(f'You found it, it is {number}')
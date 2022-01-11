import random

def shuffle(lst):
    list1 = lst.split()
    list1 = random.sample(list1, len(list1))

    return list1

def main():
    userInput = input(f'Enter numbers: ')
    list1 = shuffle(userInput)

    print(f'{list1}')

main()





    

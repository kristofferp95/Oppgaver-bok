import random

words = ["helo", "number", "children", "pizaplce", "hamburger"]
miss = 0
answer = "y"

word = words[random.randint(0, len(words))]
wordslist = list(word)
print(wordslist)
print(wordslist[0])

newword = [ "*" for x in wordslist ]
guess = "e"
index = 0

while ''.join(newword) != ''.join(word):
    newword = ''.join(newword)
    guess = str(input(f'Enter a letter in word {newword} > '))
    newword = list(newword)
    if wordslist.count(guess) > 0: 
        index = wordslist.index(guess)
        newword[index] = guess
    else:
        miss += 1

print(''.join(newword))
print(f'Corret, you missed {miss} times')
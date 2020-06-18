from random import choice
import requests

print('H A N G M A N')
print('please wait....')
word_site = 'http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
response = requests.get(word_site)
word_list = response.content.splitlines()
while True:
    entry = input('Type "play" to play the game, "exit" to quit: ')
    if entry == 'play':
        rand_word = (choice(word_list).decode('utf-8')).lower()
        rand_word_temp = rand_word
        current_word = '-' * len(rand_word)
        attempts_left = 8
        user_entries = []
        flag = 0
        while attempts_left != 0:
            print()
            print(current_word)
            inp = input('Input a letter: ')
            if len(inp) != 1:
                print('You should input a single letter')
                continue
            if inp.isalpha() & inp.islower():
                if inp in rand_word:
                    for j in range(0, rand_word.count(inp)):
                        position = rand_word.find(inp)
                        current_word = current_word[:position] + inp + current_word[position + 1:]
                        rand_word = rand_word[:position] + '.' + rand_word[position + 1:]
                        user_entries.append(inp)
                elif inp in user_entries:
                    print('You already typed this letter')
                    continue
                else:
                    print('No such letter in the word')
                    attempts_left -= 1
                    user_entries.append(inp)
                if current_word == rand_word_temp:
                    print('You guessed the word')
                    flag = 1
                    break
            else:
                print('It is not an ASCII lowercase letter')
        if flag == 1:
            print('You survived!')
            print()
        else:
            print('You are hanged!')
            print()
    elif entry == 'exit':
        break
    else:
        print('Invalid Entry!')
        continue

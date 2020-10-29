import random

cont = True
print("H A N G M A N")
s = input('Type "play" to play the game, "exit" to quit:')

while s == "play":
    print()

    lives = 8
    words = ['python', 'java', 'kotlin', 'javascript']
    current_word = random.choice(words)

    current_word_cipher = ""
    for i in range(len(current_word)):
        current_word_cipher += "-"

    input_chars = set()
    existing_chars = set(current_word)
    while lives > 0:
        print(current_word_cipher)
        char = input("Input a letter:")
        if char not in input_chars:
            if len(char) == 1:
                if char.isalpha() and char.islower():
                    if char in existing_chars:
                        for j in range(len(current_word)):
                            if current_word[j] == char:
                                if j != len(current_word):
                                    current_word_cipher = current_word_cipher[:j] + char + current_word_cipher[j + 1:]
                                else:
                                    current_word_cipher = current_word_cipher[:j] + char
                        if current_word == current_word_cipher:
                            break
                    else:
                        print("No such letter in the word")
                        lives -= 1
                    if lives == 0:
                        print("You lost!")
                    input_chars.add(char)
                else:
                    print("It is not an ASCII lowercase letter")
                    print()
                    continue
            else:
                print("You should input a single letter")
                print()
                continue
        else:
            print("You already typed this letter")
            print()
            continue
        print()

    if current_word_cipher == current_word:
        print(current_word)
        print("You guessed the word!")
        print("You survived!")

    s = input('Type "play" to play the game, "exit" to quit:')

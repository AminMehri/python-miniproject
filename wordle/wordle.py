import random 
import re



def choose_word():
    file1 = open('/home/amin/Projects/python_practice/wordle/words.txt', 'r')
    lines = file1.readlines()

    new_words = []
    for line in lines:
        res = re.search("^.....$", line)
        if res and not '.' in res.group() and not '-' in res.group() and not "'" in res.group():
            new_words.append(res.group().lower())

    target_word = random.choice(new_words)
    print(target_word)
    return target_word

def main():
    target_word = choose_word()
    while True:
        user_word = input("Enter your word:\n")
        existing_chars = []
        right_pos_chars = []

        if target_word == user_word:
            return print('*'*100, "Congratulations!!!", '*'*100)
        for char in user_word:
            if char in target_word:
                existing_chars.append(char)
        
        for index, value in enumerate(user_word):
            if user_word[index] == target_word[index]:
                right_pos_chars.append(value)

        print("Existing characters: ", existing_chars)
        print("Right position characters: ", right_pos_chars, end='\n\n')

main()
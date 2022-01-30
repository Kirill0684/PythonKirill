def int_func(word):
    word = word.capitalize()    # or word.title()
    return word


sentence = input('input sentence: ')
sentence = sentence.split()
for i in range(len(sentence)):
    int_func(sentence[i])
    print(f'{int_func(sentence[i]) }', end=" ")


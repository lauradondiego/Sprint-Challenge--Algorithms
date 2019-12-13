'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2: 
        return 0
        # ^ the word has to be at least length of 2 to contain "th"
    for i in word:
        i = []




print(count_th("lmnbthl"))
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) < 2:  # <- base case (or it will run forever!)
        return 0
        # ^ the word has to be at least length of 2 to contain "th"
    if word[0] + word[0+1] == "th":
        # ^ the indexs must be next to each other
        return 1 + count_th(str((word[1:])))
        # ^ recurisvely call the function
    else:
        return count_th(word[1:])


print(count_th("lmnbl"))  # test should print 0
print(count_th("lmnthbl"))  # test should print 1
print(count_th("lmthnblthsdf"))  # test should print 2

# for i in word:
#     i = []
#     h = i + 1
#     count_th(word-1) + count_th(word-2 )

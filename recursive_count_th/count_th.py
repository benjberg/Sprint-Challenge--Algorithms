'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # count = word.count('th')
    # return count
    count = 0
    if word.count("th") == 0:
        return count
    elif word.find("th") != -1:
        count += 1
        return count + count_th(word[word.find("th") + 2:])     
    
    
    

def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            lst.append(word)
            ctr += 1
        print("List of words with  1st and last character same\n", lst)
        return ctr
count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("Number of words having same first and last letters are:", count)

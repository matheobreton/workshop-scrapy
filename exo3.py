import copy

def anagrams(word, items):
    ret = []
    for i in items:
        good = True
        word2 = copy.copy(word)
        for j in i:
            if (j not in word2):
                good = False
                break
            else:
                word2 = word2.replace(j, "", 1)

        if (good == True and len(i) == len(word)):
            ret.append(i)
    return ret

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))




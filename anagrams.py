def anagrams(word):
    #dictFileName = 'dict/fr/ods4.txt'
    dictFileName = 'dict/en/fullable.lst'
    words = [w.rstrip() for w in open(dictFileName)]
    sword = sorted(word)
    return [w for w in words if sorted(w) == sword]

if __name__ == "__main__":
    print anagrams('FEAR')

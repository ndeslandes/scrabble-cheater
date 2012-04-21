#!/usr/bin/env python

def count_letters(word):
    count = {} 
    for letter in word:
        if letter not in count: 
            count[letter] = 0
        count[letter] += 1 
    return count 

def spellable(word, rack):
    word_count = count_letters(word)
    rack_count = count_letters(rack)
    return all([word_count[letter] <= rack_count[letter] for letter in word])  

english_score = {"A": 1, "B": 3, "C": 3, "D": 2,  "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3,
                 "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}
                 
french_score = {"A": 1, "B": 3, "C": 3, "D": 2,  "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3,
                "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

def score_word(word, score):
    return sum([score[c] for c in word])

def word_reader(filename):
    # returns an iterator
    return (word.strip().upper() for word in open(filename)) 

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2: 
        rack = sys.argv[1].strip().upper()
        try :
            language = sys.argv[2].strip().upper()
        except IndexError:
            language = 'EN'
    else:
        print """Usage: python scrabble_cheater.py <yourrack> <fr/en>"""
        exit()

    english_dictionary_filename = 'dict/en/fullable.lst'
    french_dictionary_filename = 'dict/fr/ods4.txt'
    
    if language == 'FR':
        score = french_score
        dictionary = french_dictionary_filename
    else:
        score = english_score
        dictionary = english_dictionary_filename
    
    words = word_reader(dictionary)
    scored = ((score_word(word, score), word) for word in words if set(word).issubset(set(rack)) and len(word) > 1 and spellable(word, rack))

    for score, word in sorted(scored):
        print str(score), '\t', word

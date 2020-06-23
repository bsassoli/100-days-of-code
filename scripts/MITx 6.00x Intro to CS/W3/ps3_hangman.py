#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 18:49:52 2020

@author: bernardino
"""

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return sum([x in lettersGuessed for x in secretWord])==len(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    '''
    LONG VERSION
    ___________________
    list = []
    for letter in secretWord:
        if letter in lettersGuessed:
            list.append(letter)
        else:
            list.append('_ ')
    return ''.join(list)
    '''

    # This is my oneliner after consulting the forums.
    # See above for longer version
    return ''.join([x if x in lettersGuessed else '_ ' for x in secretWord])




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    return ''.join([x for x in string.ascii_lowercase if x not in lettersGuessed])

def hangman(secretWord):

    guesses = 8
    lettersGuessed = []
    print('Welcome to the game Hangman')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))

    while guesses > 0 or isWordGuessed(secretWord, lettersGuessed) == False:
        print('-----------')
        print('You have {} guesses left.'.format(guesses))
        print('Available letters: {}'.format(getAvailableLetters(lettersGuessed)))
        guess = str(input('Please guess a letter: ')).lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            if guess in secretWord:
                lettersGuessed.append(guess)
                print('Good guess: '+ getGuessedWord(secretWord, lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed):
                    print('-----------')
                    print('Congratulations, you won!')
                    break
            else:
                lettersGuessed.append(guess)
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                guesses-=1
                if guesses == 0:
                    print('-----------')
                    print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
                    break



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman('pollo')

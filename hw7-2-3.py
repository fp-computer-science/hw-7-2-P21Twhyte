# Author Tow 11/9/2020

word = input("Please enter a word. ")

word_a = word.lower()
word1 = word_a[:]
word2 = word_a[::-1]

if word1 != word2:
    print(word + " is not a palindrome. ")
else:
    print(word + " is a palindrome. ")



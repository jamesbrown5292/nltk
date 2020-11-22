import time
#import content form nltk book
from nltk.book import *

#Concordance view shows us a word plus some context 
word = input("Enter a word and we will find it in Moby Dick ")
text1.concordance(word)

#Using the .simlar method shows words that appear in a similar context as the word
word = input("\n Enter a word and I will show words that occur in a similar context in Moby Dick ")
text1.similar(word)

input("\n Let's see how the context differs in Jane Austen. Press any key")
text2.similar(word)

#common_contexts shows us the conetxt shared by two or more words
word1 = input("\n Enter two words and we can look at the context shared by these two words in Moby Dick. Enter word 1: ")
word2 = input("\nEnter word 2: ")
text1.common_contexts([word1, word2])

#Generate texts in a syle with .generate()
print("Now, let's generate a text in the style of the inaugural address corpus")
text4.generate()
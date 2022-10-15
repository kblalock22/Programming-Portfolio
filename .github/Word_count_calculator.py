#This is a program that computes the word count for a given string provided by the user. Its real-world application would be to calculate the word count of an essay to ensure it meets given requirements.

text = input("Type your essay here: ")

word_list = text.split()

word_count = str(len(word_list))

if word_count == 1:
    print("Your essay is " + word_count + " total word.")
else:
    print("Your essay is " + word_count + " total words.")
    
    




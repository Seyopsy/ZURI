# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


#def find_anagram(word, anagram):
    # [assignment] Add your code here

    #get input from user
word=input("Type the Word ")

    #get input from user
anagram=input("Type the Possible Anagram  ")

#convert to lower case,python is case sensitive 
word=word.lower()
anagram=anagram.lower()

    #length of first word
arrange_word=sorted(word)

    #arrange first word
arrange_anagram=sorted(anagram)

if(arrange_word==arrange_anagram):
    print(True)
else: 
    print(False)

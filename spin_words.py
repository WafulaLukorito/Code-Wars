
"""Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
    """

def spin_words(sentence):
    # Your code goes here
    splits = sentence.split()
    for i in range (0, len(splits)):
        if len(splits[i]) > 4:
            splits[i] = splits[i][::-1]

    ' '.join(splits)
            
        
    return splits


phrase =  "Hey fellow warriors" 
spin = spin_words(phrase)
print (spin)
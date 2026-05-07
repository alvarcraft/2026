# User types a sentence, program tells them how many words are in it, how many characters, 
# and how many characters without spaces.
# You have everything you need already — len(), .split(), .replace().

#characters no space = cns
#characters with space = cws
sentence = input("")
words = len(sentence.split(" "))
cns = len(sentence.replace(" ", ""))
cws = len(sentence)
print(f"amount of words: {words}, characters with space: {cws}, characters no space {cns}")
#print(words)
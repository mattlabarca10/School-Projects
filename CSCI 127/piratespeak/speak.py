# Extras completed: pirate.dat, handles upper/lower cases, and advanced translations 

pirate = open('pirate.dat').read()       # opens and reads all files    
inp = open('input.txt').read()
input = inp.lower().split()              # each word in input is a list
psplit = pirate.split('\n')              # each word in pirate is a list
piratespeak = {}
for word in psplit:                      # converting list of pirate into a dictionary
    piratespeak.update({word[:word.index(":")]:word[word.index(':')+1:]})  
keys = []
for word in psplit:                      # listing all the keys in dictionary into a list
    keys.append(word[:word.index(":")])
npinput = []
for word in input:                       # making list of input with no punctuation to be put back later
    if ',' in word or '.' in word or '!' in word:
        npinput.append(word[:-1])
    else:
        npinput.append(word)

newstory = []
ind = 0
for word in npinput:  # loops through npinput, replaces certain words/phrases to piratespeak using the dictionary
    if word in keys: 
        newstory.append(piratespeak[word])
    elif word == "<surprise>":
        newstory.append("Blow me down!")
    elif word == "<drinkwithcrew>":
        newstory.append("Splice the mainbrace!")
    else:
        newstory.append(word)  
    if ind == 0 or word == 'i' or '.' in input[ind-1] or '!' in input[ind-1]:  # properly re-capitalizing
        newstory[ind] = newstory[ind].capitalize() 
    if "." in input[ind]:               # adding back punctuation
        newstory[ind] = newstory[ind] + "."
    elif "," in input[ind]:
        newstory[ind] = newstory[ind] + ","
    elif "!" in input[ind]:
        newstory[ind] = newstory[ind] + "!"
    ind+=1
final = ' '.join(newstory)              # making final story into one string

print(final)



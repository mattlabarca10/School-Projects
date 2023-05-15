import random
# Thomas H helped me with the open() and read() functions
s = open('story.dat')           # opens and reads all files    
a = open('adj.dat')
na = open('nounanimal.dat')
nn = open('nounname.dat')
v = open('verbs.dat')
sread = s.read()
aread = a.read()
naread = na.read()
nnread = nn.read()
vread = v.read()
alist = aread.split()           # turns files into lists       
nalist = naread.split()
nnlist = nnread.split()
vlist = vread.split()

def randAdj():                                      # random adjective from adj.dat
    return alist[random.randrange(len(alist))]

def randNounName():                                 # random name from nounname.dat
    return nnlist[random.randrange(len(nnlist))]

def randNounAnimal():                               # random animal from nounanimal.dat
    return nalist[random.randrange(len(nalist))]

def randVerb():                                     # random verb from verbs.dat
    return vlist[random.randrange(len(vlist))]

def madlibs(story):             # Thomas H helped me with the structure of this method
    new = sread.split()         # new list of the story
    ind = 0                     # index tracker
    indName = -1                # keeps track if a name is established yet, and what index it is
    for i in new:                                 
        if "<NOUNName>" in i:                     # names
            if indName == -1:                     # if this is the first time name is used
                new[ind] = randNounName()         # calls premade random function at index of <NOUNName> (repeated)
                indName = ind                
            else:                                 # else, use the name from the index of first use, so the character is consistent
                new[ind] = new[indName]
            if "." in i:                          # if there was punctuation we add it back here (repeated)
                new[ind] = new[ind] + "."
            elif "," in i:
                new[ind] = new[ind] + ","
        elif "<NOUNAnimal>" in i:                 # animals
            new[ind] = randNounAnimal().lower()
            if(ind == 0 or '.' in new[ind-1]):    # if it's the first letter of sentence, capitalize it (repeated)
                new[ind] = new[ind].capitalize()
            if "." in i:
                new[ind] = new[ind] + "."
            elif "," in i:
                new[ind] = new[ind] + ","
        elif "<VERB>" in i:                       # verbs
            new[ind] = randVerb().lower()
            if(ind == 0 or '.' in new[ind-1]):
                new[ind] = new[ind].capitalize()
            if "." in i:
                new[ind] = new[ind] + "."
            elif "," in i:
                new[ind] = new[ind] + ","
        elif "<ADJ>" in i:                        # adjectives
            new[ind] = randAdj().lower()
            if(ind == 0 or '.' in new[ind-1]):
                new[ind] = new[ind].capitalize()
            if "." in i:
                new[ind] = new[ind] + "."
            elif "," in i:
                new[ind] = new[ind] + ","
        ind+=1
    return ' '.join(new)                          # turns new list back into a string and returns

print(madlibs(sread))


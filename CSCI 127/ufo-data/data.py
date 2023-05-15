# Description: 
#   This program analyzes UFO sightings data from the National UFO Reporting Center (NUFORC).
#   The data is stored in a CSV file, and the program will read the data from the file.
#   The program will then analyze the time of day and state of each of the sightings.
#   The top ten states with the most sightings will be displayed and the number of sightings
#   by time of day will be displayed in a graph.

# Extras Completed:
#   Used multiple aspects of a single data source in analysis
#   Used Matplotlib to visualize part of analysis.

import matplotlib.pyplot as plt

# Opens and reads the data from the CSV file of all US UFO sightings. Splits each new line into values of a list
ufo = open('ufosightings.csv', 'r').read()
ufo = ufo.split('\n')

# Detects where the time is in each line and creates a seperate list of frequency of sightings per hour
timeTrack = []
for num in range(0,24):
    timeTrack.append(0)
for data in ufo:
   for num in range(0,24):
       if ':' in data and num == int(data[(data.index(':')-2):(data.index(':'))]):
              timeTrack[num]+=1

# Converts list into dictionary
timeTracker = {}
for num in timeTrack:
    timeTracker.update({timeTrack.index(num):num})

# Creates graph displaying the number of sightings by time of day
plt.plot([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], timeTrack, color='g')
plt.xlabel('Time of Day')
plt.ylabel('Number of Sightings')
plt.title('UFO Sightings by Time of Day')
plt.show()

# Opens and reads the data from the file of all state abbreviations and splits each word into a list
states = open('states.dat', 'r').read()
stateslist = states.split(", ")

# Detects where the state is in each line and creates a seperate list of frequency of sightings per state
stateTrack = []
for num in range(0,50):
    stateTrack.append(0)
for data in ufo:
    ind = 0
    for state in stateslist:
        if state + ',us' in data:
            stateTrack[ind] += 1
        ind+=1

# Assigns state abbreviations to the number of sightings in the state 
stateTracker = {}
ind = 0
for state in stateslist:
    stateTracker.update({state:stateTrack[ind]})
    ind+=1

# Calculates the top ten states with the most sightings
stateTrackCopy = stateTrack
topten = {}
for num in range(0,10):
    max = stateTrack[0]
    ind = 0
    for value in stateTrackCopy:
        if stateTrackCopy[ind] > max:
            max = stateTrackCopy[ind]
        ind+=1
    for keys in stateTracker:
        if stateTracker.get(keys) == max:
            topten.update({keys:max})
    stateTrackCopy.remove(max)

# Opens and reads the data of full state names with abbreviations and splits each new line into values of a list
fullstates = open('fullstates.dat', 'r').read()
fullstates = fullstates.split('\n')

# Creates a dictionary with all states with its abbreviation
fullstatesdict = {}
for word in fullstates:                      
    fullstatesdict.update({word[:word.index(':')]:word[word.index(':')+1:]})

# Modifies the topten dictionary by creating a new dictionary that has the full state name instead of abbreviation
# I realize that if I just used a file of full state names I could have saved a lot of time
newtopten = {}
for tenkey in topten:                    
    for statekey in fullstatesdict:
        if tenkey == fullstatesdict[statekey]:
            newtopten.update({statekey:topten[tenkey]})

# Creates a multiline string to display the top ten sightings uniformly
finaltopten = """"""
for key in newtopten:
    finaltopten += key + ': ' + str(newtopten[key]) + '\n'
print("The top ten states with the most UFO sightings are:") 
print(finaltopten)
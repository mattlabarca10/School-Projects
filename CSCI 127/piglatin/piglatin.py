"""
def bondify(name):
  result = ""
  location = name.find(' ')
  first = name[0].upper() + name[1:location]
  last = name[location+1].upper() + name[location+2:]
  result = last + ", " + first + " " +last
  return result

print(bondify("Matthew LaBarca"))
print(bondify("james bond"))
"""

def piglatinify(word):
  result = ""
  first = word[0]
  first = str(first)
  last = word[len(word)-1]
  last = str(last)
  punc = False
  if word[0] == word[0].upper():
    capital = True
  else:
    capital = False
  if last in '.!?,':
     punc = True
  a = len(word)-1
  if (punc == True):     
    if first in 'aeiouAEIOU':
      result = (word[0:a]+"yay"+last).lower()
    else:
      result = (word[1:a]+word[0]+"ay"+last).lower()
  else: 
    if first in 'aeiouAEIOU':
      result = (word[0:]+"yay").lower()
    else:
      result = (word[1:]+word[0]+"ay").lower()
  if capital:
    result = result.capitalize()
  return result

print(piglatinify("Family."))
print(piglatinify("Than!"))
print(piglatinify("apple,"))
print(piglatinify("Octopus"))
print(piglatinify("Matthew?"))
print(piglatinify("You're"))

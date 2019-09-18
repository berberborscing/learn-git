#
# Decription: This program will analize the upper and lower case content of
# a given string.
#



sampleString = "We the People of the United States, in Order+ to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America."

"""
## 1) Start by counting the number of upper, lower, and other characters inthe provided string. Print your results.
"""

lowers = 0;
uppers = 0;
not_letters = 0;

for char in sampleString:
  if char.islower():
    new_string += char.upper()
    lowers += 1
  if char.isUpper():
    new_string += char.lower()
    uppers += 1
  else:
    newstring += char
    not_letters += 1
print(lowers, uppers, not_letters)

# 2) Next, invert the case of all of the text in the sample string. Print the resulting string.

print(newstring)

# 3) Place all vowels in one list. 

vowel_list = []
consonant_list = []
for char in sampleString:
  if char in "aeiouy":
    vowel_list.append(char)
  elif char in "bcdfghjklmnpqrstvwxz"
    consonant_list.append(char)
  

# 4) Place all consonant in another list. 

# 5) Find the decimal value of each character and place all characters that are multiples of 3 in another list.


###
# Name and EID:Nathan Swindall 

#########
# Problem 1a:
>>> import re
>>> import codecs
>>> f=codecs.open(r"C:\Users\Nathan\Desktop\36.txt", encoding="utf-8")
>>> 
>>> War = f.readlines()
>>> s = "".join(War)
>>> t= s.split()
>>> count = 0
b>>> for line in r:
	if re.search("^[^aeiouAEIUO]*[aeiouyAEIOUY]+[^aeiouyAEIOUY]*$", line):
		count = count + 1

>>> count
38797
#########
# Problem 1b: Two examples of words that do not fit this definition of a one syllable
# word are the word "state" which is a one syllable word that has a CVCV sequence not defined
# by our definition and the word "World" which is a two syllable word but is defined as a
# one syllable word. 

#########
# Problem 2:
# a)
>>> t= T.split()
>>> h=[]
>>> for word in t:
	if word.endswith(","):
		h.append(word.replace(",",""))
	else:
		h.append(word)

>>> u=[]
>>> for word in h:
	if word.endswith("]"):
		u.append(word.replace("]",""))
	else:
		u.append(word)

		
>>> o=[]
>>> for word in u:
	if word.startswith("#"):
		o.append(word.replace("#",""))
	else:
		o.append(word)

>>> for line in o:
	if re.search("^\d+$", line):
		print(line)
	elif re.search("^-\d+$", line):
		print(line)
	elif re.search("^-\.\d+$", line):
		print(line)
	elif re.search("^\.\d+$", line):
		print(line)
	elif re.search("^-\d+\.\d+$", line):
		print(line)
	elif re.search("^\d+\.\d+$", line):
		print(line)
	elif re.search("^(\d+)*,*(\d+)*,*(\d+)*,*(\d+)*,*\d+$", line):
		print(line)

# c
>>> for line in t:
	if re.search("forget", line):
		print(line)
	elif re.search("forgot", line):
		print(line)
#d
>>> for line in t:
	if re.search("^[aeiou]{3}$|[^aeiou][aeiou]{3}[^aeiou]|[^aeiou][aeiou]{3}$|^[aeiou]{3}[^aeiou]", line):
		print(line)		
		
		

#########
# You can do problems 3-5 on paper, if you like. 
# But please don't forget to put your name on the paper!


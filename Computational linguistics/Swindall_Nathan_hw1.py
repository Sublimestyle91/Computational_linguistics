########
# Your name and EID:
Nathan Swindall Nts279
#########
# Problem 1:
(c) you can't have a dash in a variable
(d) you cannot start a variable with numbers
(e) you cannot use this because it is already used in python for something else
(h) you cannot use this becuase it has a space in the variable name
extra credit: you can use (f) as a valid variable name, but you shouldn't becuase python assigns it something already.


#########
# Problem 2:
text = "After the glimpse I had had of the Martians emerging from the cylinder in which they had come to the earth from their planet, a kind of fascination paralysed my actions. I remained standing knee-deep in the heather, staring at the mound that hid them. I was a battleground of fear and curiosity.I did not dare to go back towards the pit, but I felt a passionate longing to peer into it. I began walking, therefore, in a big curve, seeking some point of vantage and continually looking at the sand heaps that hid these new-comers to our earth. Once a leash of thin black whips, like the arms of an octopus, ﬂashed across the sunset and was immediately withdrawn, and afterwards a thin rod rose up, joint by joint, bearing at its apex a circular disk that spun with a wobbling motion. What could be going on there?"
text.count("of")

#########
# Problem 3:
>>> words= text.split()
>>> h= []
>>> for word in words:
	if "." or "," or "?" in word:
		h.append(word.replace(".","").replace(",","").replace("?",""))
	else:
		h.append(word)

#########
# Problem 4:
counter = 0
>>> for ing in h:
	if ing.endswith("ing"):
		counter = counter + ing.count("ing")

#########
# Problem 5:
l=[]
>>> for suffix in h:
	if suffix.endswith("ing"):
		s=list(suffix)
		del s[-3:]
		string1="".join(s)
		l.append(string1)
	elif suffix.endswith("ed"):
		x=list(suffix)
		del x[-2:]
		string2="".join(x)
		l.append(string2)
	elif suffix.endswith("s"):
		t=list(suffix)
		del t[-1]
		string3="".join(t)
		l.append(string3)
	else:
		l.append(suffix)

#########
# Problem 6:
import codecs
f=codecs.open(r"C:\Users\Nathan\Desktop\768.txt", encoding = "utf-8")
>>> bronte_string=f.read()
>>> bronte_string.index("s**")
>>> bronte_string.index("***E")
>>> bronte_string[553:613]
>>> bronte_string[662592:662650]
>>> bronte_string[614:662591]



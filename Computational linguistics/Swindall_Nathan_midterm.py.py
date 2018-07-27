# Midterm exam answers
#
# Name:Nathan Swindall
# EID: nts279

#########
# Problem 1:
def summed_wordlength(word):
	return(len("".join(word)))


#########
# Problem 2:
import codecs
f=codecs.open(r"C:\Users\Nathan\Desktop\count of monte cristo.txt", encoding="utf-8")
comc = f.readlines()
import re
for line in comc:
	if re.search("(^|[^A-Za-z])[Ss]tand([^A-Za-z]|$)", line):
		print(line)
	elif re.search("(^|[^A-Za-z])[Ss]tands([^A-Za-z]|$)", line):
		print(line)
	elif re.search("(^|[^A-Za-z])[Ss]tood([^A-Za-z]|$)", line):
		print(line)
	elif re.search("(^|[^A-Za-z])[Ss]tanding([^A-Za-z]|$)", line):
		print(line)

#########
# Problem 3a:
import nltk
from nltk.corpus import brown
brown_tagged_words = brown.tagged_words(categories = "news")
h=[]
for item in brown_tagged_words:
	word, tag = item
	h.append(tag[:2])


#########
# Problem 3b:
import codecs
f=codecs.open(r"C:\Users\Nathan\Desktop\count of monte cristo.txt", encoding="utf-8")
comc= f.readlines()
k = " ".join(comc)
h=[]
for word in k.split():
	if word.endswith("."):
		h.append(word.replace(".",""))
	elif word.endswith("?"):
		h.append(word.replace("?", ""))
	elif word.endswith(","):
		h.append(word.replace(",",""))
	else:
		h.append(word)


g= []
for word in h:
	g.append(word.lower())

import re
y=[]
for word in g:
	if word[:2] == "in" and re.search("in[a-z]", word):
		s = list(word)
		del s[:2]
		string1="".join(s)
		y.append(string1)
#Two words where "in" is a prefix are informed and explicable. Two words where "in"
#is not a word are inner and ink. It seems the only way I can think of where one could
#avoid finding words where "in" is not a prefix is to have some sort of dictionary where		
#there are words without the "in" prefix. Then we refer are list to this dictionary to check
#if the deprefixed froms are there.
#########
# Problem 4:
import nltk
from nltk.corpus import brown
Nathan = brown.tagged_words(categories ="news")
Thomas = list(Nathan)
y=[]
for word in Thomas:
	palabra, tags = word
	if "IN" in tags:
		y.append(palabra)

counts={}
for word in y:
	if word not in counts:
		counts[word]= 0
	counts[word]= counts[word] + 1

	
prepositions = list(counts.keys())

Q=[]
for word in Thomas:
	palabra, tags = word
	if "V" in tags:
		Q.append(palabra)

		
counts2={}
for word in Q:
	if word not in counts2:
		counts2[word]= 0
	counts2[word]= counts2[word] + 1

	
Verbs = list(counts2.keys())
prepositions_preceding={}
words = brown.words(categories = "news")
bigrams = nltk.bigrams(words)
N={}
for w1, w2 in bigrams:
	if w2 in prepositions and w1 in Verbs:
		if w1 in N and w2 not in list(N[w1]):
			N[w1].append(w2)
		elif w1 in N and w2 in list(N[w1]):
			pass
		else:
			N[w1] = [w2]

			
y= list(N.keys())
G={}
for key in y:
	G[key]= len(N[key])

def second_of_pair(tuple):
	return tuple[1]

W= sorted(G.items(), key = second_of_pair, reverse= True)

#The verb with the most prepositions after it is "came". It has fifteen prepositions 
#after it and they are ['to', 'in', 'into', 'during', 'out', 'on', 'off', 'up', 'a', 'at', 'along', 'under', 'from', 'by', 'after']


#########
# Problem 5a:
import nltk
import sys
import string
import codecs
f=codecs.open(r"C:\Users\Nathan\Desktop\Bram.txt", encoding="utf-8")
Bram = f.readlines()
lines_in_Bram = " ".join(Bram)
Words_in_Bram = [ w.strip(string.punctuation).lower() for w in lines_in_Bram.split() ]
freq_Bram = nltk.FreqDist(Words_in_Bram)
freq_Bram.most_common(10)
#This gives you the ten most frequent words and their frequency
[('the', 8037), ('and', 5896), ('i', 4712), ('to', 4540), ('of', 3738), ('a', 2962), ('in', 2558), ('he', 2543), ('that', 2455), ('it', 2141)]
bigrams ={}
Words_in_Bram = ["START"] + Words_in_Bram + ["ENDS"]
for index, word in enumerate(Words_in_Bram):
	if index < len(Words_in_Bram) -1:
		w1 = Words_in_Bram[index]
		w2 = Words_in_Bram[index+1]
		bigram = (w1,w2)
		if bigram in bigrams:
			bigrams[bigram] = bigrams[bigram] + 1
		else:
			bigrams[bigram]=1
def second(tuple):
	return tuple[1]
y = sorted(bigrams.items(), key = second, reverse = True)
y[:10]
#This gives you the ten most frequent bigrams and their frequecies.
[(('of', 'the'), 896), (('in', 'the'), 629), (('', ''), 526), (('to', 'the'), 383), (('and', 'the'), 340), (('and', 'i'), 329), (('on', 'the'), 324), (('it', 'was'), 311), (('it', 'is'), 303), (('van', 'helsing'), 299)]


#########
# Problem 5b:
num_Bram= len(Words_in_Bram)
count_there= Words_in_Bram.count("there")
count_thereis = bigrams["there","is"]
count_is = Words_in_Bram.count("is")
count_a = Words_in_Bram.count("a")
count_vampire = Words_in_Bram.count("vampire")
count_in= Words_in_Bram.count("in")
count_the= Words_in_Bram.count("the")
count_room=Words_in_Bram.count("room")
count_isa= bigrams["is","a"]
count_avampire=bigrams["a", "vampire"]
count_vampirein=bigrams["vampires","in"]
count_vampirein=bigrams["vampire","in"]
count_inthe=bigrams["in","the"]
count_theroom=bigrams["the","room"]
zz= count_there/num_Bram
xx= count_thereis/count_there
cc= count_isa/count_is
vvv= count_avampire/count_a
bb= count_vampirein/count_vampire
nn= count_inthe/count_in
mm=count_theroom/count_the
Probability= zz*xx*cc*vvv*bb*nn*mm

#########
# Problem 5c:
freq_Bramuingram= nltk.FreqDist(Words_in_Bram)
def unigram_pro(word):
	return freq_Bramuingram[word]/ num_Bram
cfreq_Bram = nltk.ConditionalFreqDist(nltk.bigrams(Words_in_Bram))
cprob_Bram = nltk.ConditionalProbDist(cfreq_Bram, nltk.MLEProbDist)
Prob= unigram_pro("there")*cprob_Bram["there"].prob("is")*cprob_Bram["is"].prob("a")*cprob_Bram["a"].prob("vampire")*cprob_Bram["tvampire"].prob("in")*cprob_Bram["in"].prob("the")*cprob_Bram["the"].prob("room")



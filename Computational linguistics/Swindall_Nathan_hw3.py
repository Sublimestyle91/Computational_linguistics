#Name: Nathan Swindall
#EID: Nts279

#########
# Problem 1:
import nltk
brown_news = nltk .corpus . brown . tagged_words ( categories="news")
y= list(brown_news)
words_and_tags=[]
for word,thing in y:
	words_and_tags.append((word.lower(),thing))
just_words=[]
for word, thing in words_and_tags:
	just_words.append(word)	
counts= {}
for word in just_words:
	    if  word not in counts:
		    counts[word] = 0
	    counts[ word ] = counts[ word ] + 1
def second_of_pair(tuple):
	return tuple[1]
frequency_sorted=sorted(counts.items(), key = second_of_pair, reverse = True)
frequency_sorted[:10]
[('the', 6386), (',', 5188), ('.', 4030), ('of', 2861), ('and', 2186), ('to', 2144), ('a', 2130), ('in', 2020), ('for', 969), ('that', 829)]
#The most frequent word is the word the.
just_tags=[]
for word, thing in words_and_tags:
    just_tags.append(thing)

	
counts2={}
for word in just_tags:
	if  word not in counts2:
		counts2[word] = 0
	counts2[ word ] = counts2[ word ] + 1

	    
frequency_sorted_tags=sorted(counts2.items(), key = second_of_pair, reverse = True)
frequency_sorted_tags[:5]
[('NN', 13162), ('IN', 10616), ('AT', 8893), ('NP', 6866), (',', 5133)]
#The most frequent tag is NN
#########
# Problem 2a:
h={}
for word,thing in words_and_tags:
    if word not in h:
		h[word]= [thing]
    if thing not in h[word]:
		h[word].append(thing)

		
words_and_alltags=[]
 
for keys,values in h.items():
    words_and_alltags.append((keys,values))

just_alltags=[]
for keys,values in words_and_alltags:
    just_alltags.append(values)

	
counter=0
for words in just_alltags:
    if len(words) > 1:
	    counter = counter + 1

		
counter
2166
# 2166 words are ambiogous.
#########
# Problem 2b:
counts3={}
words_tagcount=[]
for words,alltags in words_and_alltags:
    words_tagcount.append((words, len(alltags)))

	
frequency_sorted_alltags=sorted(words_tagcount, key = second_of_pair, reverse = True)frequency_sorted_alltags[:2]
[('to', 7), ('house', 7)]
# The words with the most POS-tags are to and house. 

#########
# Problem 3:
brown_sentences = nltk . corpus . brown . tagged_sents ( categories="news")
Sentences_house=[]
Sentences_to=[]
a=0
b=0
c=0
d=0
e=0
f=0
g=0
Sentences_house=[]
for word in brown_sentences:
	if ('House', 'NN-TL') in word:
		a=a+1
		if a<2:
			Sentences_house.append(word)
	if ('house', 'NN') in word:
		b=b+1
		if b<2:
			Sentences_house.append(word)
	if ('house', 'NN-HL')  in word:
		c=c+1
		if c<2:
			Sentences_house.append(word)
	if ('House', 'NP-TL-HL') in word:
		d=d+1
		if d<2:
			Sentences_house.append(word)
	if ('House', 'NP') in word:
		e=e+1
		if e<2:
			Sentences_house.append(word)
	if ('House', 'NN-TL-HL')  in word:
		f=f+1
		if f<2:
			Sentences_house.append(word)
	if ('house', 'VB')   in word:
		g=g+1
		if g<2:
			Sentences_house.append(word)
Sentences_house
[[('Schley', 'NP'), ('County', 'NN-TL'), ('Rep.', 'NN-TL'), ('B.', 'NP'),
('D.', 'NP'), ('Pelham', 'NP'), ('will', 'MD'), ('offer', 'VB'), ('a', 'AT'),
('resolution', 'NN'), ('Monday', 'NR'), ('in', 'IN'), ('the', 'AT'), ('House', 'NN-TL'),
('to', 'TO'), ('rescind', 'VB'), ('the', 'AT'), ("body's", 'NN$'),
('action', 'NN'), ('of', 'IN'), ('Friday', 'NR'), ('in', 'IN'), ('voting', 'VBG'),
('itself', 'PPL'), ('a', 'AT'), ('$10', 'NNS'), ('per', 'IN'), ('day', 'NN'),
('increase', 'NN'), ('in', 'IN'), ('expense', 'NN'), ('allowances', 'NNS'),
('.', '.')], [('The', 'AT'), ('house', 'NN'), ('passed', 'VBD'), ('finally', 'RB'),
(',', ','), ('and', 'CC'), ('sent', 'VBD'), ('to', 'IN'), ('the', 'AT'),
('Senate', 'NN-TL'), (',', ','), ('a', 'AT'), ('bill', 'NN'), ('extending', 'VBG'),
('the', 'AT'), ('State', 'NN-TL'), ('Health', 'NN-TL'), ("Department's", 'NN$-TL'),
('authority', 'NN'), ('to', 'TO'), ('give', 'VB'), ('planning', 'VBG'),
('assistance', 'NN'), ('to', 'IN'), ('cities', 'NNS'), ('.', '.')],
[('Hood', 'NN-HL'), ('flies', 'VBZ-HL'), ('over', 'IN-HL'), ('house', 'NN-HL')],
[('House', 'NP-TL-HL'), ('throws', 'VBZ-HL'), ('wild', 'RB-HL')], [('Pete', 'NP'),
('Ward', 'NP'), ('was', 'BEDZ'), ('sent', 'VBN'), ('in', 'RP'), ('for', 'IN'),
('House', 'NP'), ('and', 'CC'), (',', ','), ('after', 'CS'), ('failing', 'VBG'),
('in', 'IN'), ('a', 'AT'), ('bunt', 'NN'), ('attempt', 'NN'), (',', ','),
('popped', 'VBD'), ('to', 'IN'), ('Howser', 'NP'), ('on', 'IN'), ('the', 'AT'),
('grass', 'NN'), ('back', 'RB'), ('of', 'IN'), ('short', 'JJ'), ('.', '.')], [('turmoil', 'NN-HL'),
('in', 'IN-HL'), ('the', 'AT-HL'), ('House', 'NN-TL-HL')], [('Last', 'AP'), ('year', 'NN'), ('Beyeler', 'NP'),
('arranged', 'VBD'), ('to', 'TO'), ('sell', 'VB'), ('$1,500,000', 'NNS'), ('worth', 'JJ'), ('of', 'IN'),
('Klees', 'NPS'), ('to', 'IN'), ('the', 'AT'), ('state', 'NN'), ('of', 'IN'), ('North', 'JJ-TL'),
('Rhine-Westphalia', 'NP-TL'), (',', ','), ('which', 'WDT'), ('will', 'MD'), ('house', 'VB'), ('them', 'PPO'),
('in', 'IN'), ('a', 'AT'), ('museum', 'NN'), ('that', 'WPS'), ('is', 'BEZ'), ('yet', 'RB'), ('to', 'TO'),
('be', 'BE'), ('built', 'VBN'), ('.', '.')]]

a=0
b=0
c=0
d=0
e=0
f=0
g=0

for word in brown_sentences:
	if ('to', 'TO') in word:
		a=a+1
		if a<2:
			Sentences_to.append(word)
	if ('to', 'IN') in word:
		b=b+1
		if b<2:
			Sentences_to.append(word)
	if ('to', 'IN-HL')  in word:
		c=c+1
		if c<2:
			Sentences_to.append(word)
	if ('to', 'TO-HL') in word:
		d=d+1
		if d<2:
			Sentences_to.append(word)
	if ('to', 'IN-TL') in word:
		e=e+1
		if e<2:
			Sentences_to.append(word)
	if ('To', 'TO-TL')  in word:
		f=f+1
		if f<2:
			Sentences_to.append(word)
	if ('to', 'NPS')   in word:
		g=g+1
		if g<2:
			Sentences_to.append(word)

Sentences_to
[[('The', 'AT'), ('September-October', 'NP'), ('term', 'NN'), ('jury', 'NN'), ('had', 'HVD'), ('been', 'BEN'),
('charged', 'VBN'), ('by', 'IN'), ('Fulton', 'NP-TL'), ('Superior', 'JJ-TL'), ('Court', 'NN-TL'),
('Judge', 'NN-TL'), ('Durwood', 'NP'), ('Pye', 'NP'), ('to', 'TO'), ('investigate', 'VB'), ('reports', 'NNS'),
('of', 'IN'), ('possible', 'JJ'), ('``', '``'), ('irregularities', 'NNS'), ("''", "''"), ('in', 'IN'),
('the', 'AT'), ('hard-fought', 'JJ'), ('primary', 'NN'), ('which', 'WDT'), ('was', 'BEDZ'), ('won', 'VBN'),
('by', 'IN'), ('Mayor-nominate', 'NN-TL'), ('Ivan', 'NP'), ('Allen', 'NP'), ('Jr.', 'NP'), ('.', '.')],
[('It', 'PPS'), ('recommended', 'VBD'), ('that', 'CS'), ('Fulton', 'NP'), ('legislators', 'NNS'), ('act', 'VB'),
('``', '``'), ('to', 'TO'), ('have', 'HV'), ('these', 'DTS'), ('laws', 'NNS'), ('studied', 'VBN'), ('and', 'CC'),
('revised', 'VBN'), ('to', 'IN'), ('the', 'AT'), ('end', 'NN'), ('of', 'IN'), ('modernizing', 'VBG'),
('and', 'CC'), ('improving', 'VBG'), ('them', 'PPO'), ("''", "''"), ('.', '.')], [('Cost', 'NN-HL'),
('up', 'RP-HL'), ('to', 'IN-HL'), ('$37', 'NNS-HL'), ('a', 'AT-HL'), ('year', 'NN-HL')],
[('Three', 'CD-HL'), ('groups', 'NNS-HL'), ('to', 'TO-HL'), ('meet', 'VB-HL')], [('On', 'IN'),
('the', 'AT'), ('clock', 'NN'), ('given', 'VBN'), ('him', 'PPO'), ('was', 'BEDZ'),
('the', 'AT'), ('inscription', 'NN'), (',', ','), ('``', '``'), ('For', 'IN-TL'), ('Outstanding', 'JJ-TL'),
('Contribution', 'NN-TL'), ('to', 'IN-TL'), ('Billiken', 'NP-TL'), ('Basketball', 'NN-TL'), (',', ','),
('1960-61', 'CD'), ("''", "''"), ('.', '.')], [('Last', 'AP'), ('October', 'NP'), ('he', 'PPS'), ('gave', 'VBD'),
('a', 'AT'), ('public', 'JJ'), ('speech', 'NN'), ('in', 'IN'), ('Washington', 'NP'), (',', ','), ('D.C.', 'NP'),
('entitled', 'VBD'), ('``', '``'), ('Are', 'BER-TL'), ('Women', 'NNS-TL'), ('Here', 'RB-TL'), ('To', 'TO-TL'),
('Stay', 'VB-TL'), ("''", "''"), ('?', '.'), ('?', '.')], [('Also', 'RB'), ('noted', 'VBN'), ('are', 'BER'),
('the', 'AT'), ('marriages', 'NNS'), ('of', 'IN'), ('Elizabeth', 'NP'), ('Browning', 'NP'), (',', ','),
('daughter', 'NN'), ('of', 'IN'), ('the', 'AT'), ('George', 'NP'), ('L.', 'NP'), ('Brownings', 'NPS'),
(',', ','), ('to', 'NPS'), ('Austin', 'NP'), ('C.', 'NP'), ('Smith', 'NP'), ('Jr.', 'NP'), (';', '.'),
(';', '.')]]
			



			

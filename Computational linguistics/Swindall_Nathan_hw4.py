# Name: Nathan Swindall
# Ut EID:Nts279

#########
# Problem 1:
#   P(both Alice and Bob put the same tag for a word) = P(Alice(Dt) and Bob(Dt))+ P(Alice(NN) and Bob(NN)) + P(Alice(VB) and Bob(VB))=
#   (.5)(.5) + (.3)(.3) + (.2)(.2) = .38
#   The probability that both use the same tag for a word is 38%.


#########
# Problem 2:
#1)Bomb suspects missing girls?
#   The two readings I have for this sentence are that the bomb suspects
#   might be the missing girls and that if you personify the bomb or it is a proper noun it suspects
#   the missing girls.
#   Bomb NN/ suspects V/ missing JJ/ girls NN
#   Bomb JJ/ suspects NN/ missing JJ/ girls NN ( intended reading)
#   Because there are two ways to tag it depending on the interpretation
#   taggin it gets rid of the ambiguity. 
#2)Anderson Cooper grills Bernie Sanders on Cuba
#   The intended reading is that Anderson Cooper is questioning Bernie Sanders harshly
#   on the topic of Cuba. The other reading (maybe) is that Anderson Cooper is literally
#   grilling sanders on cuban soil. 
#   Anderson Cooper NNP/ grills VB/ Bernie Sanders NNP/ on P/ Cuba NNP
#   Tagging the words does not  get rid of ambiguity
#3)Community Easter egg hunts saturday.
#   The intended reading is that there are going to be multiple communityeaster egg hunt events
#   on saturday. The other reading is to personify the egg so that it will be hunting
#   on saturady.
#   Community JJ/ Easter JJ/ egg jj/ hunts NN/ saturday RB
#   Community JJ/ Easter JJ/ egg NN/ hunts VB/ saturday RB
#   Because there are two ways to tag this depending on the reading it
#   seems that tagging the words gets rid of ambiguity


#########
# Problem 3:
import nltk
from nltk.corpus import brown
import re
brown_tagged_sents= brown.tagged_sents(categories='adventure')
patterns = [(r'.*ese$', 'JJ'),                  #common adjective ending
            (r'.*ify$', 'VB'),                  #common Verb ending
            (r'.*ful$', 'JJ'),                  #common adjective ending
            (r'.*ive$', 'JJ'),                  #common adjective ending
            (r'.*less$', 'JJ'),                 #common adjective ending
            (r'.*al$', 'JJ'),                   #common adjective ending
            (r'.*ic$', 'JJ'),                   #common adjective ending
            (r'.*ous$', 'JJ'),                  #common adjective ending
            (r'.*(ible|able)$', 'JJ'),          #common adjective ending
            (r'.*ly$', 'RB'),                   #common adverb ending
            (r'.*is$', 'BEZ'),                  #3rd person of the verb to be
            (r'^([Ss]he|[Hh]e)|it$', 'PPS'),    #3rd person pronouns
            (r'^[oO]f$', 'IN'),                 #common pronoun
            (r'^[aA]$|[aA]n$', 'AT'),           #common article
            (r'^[tT]he$', 'AT'),                #common articel
            (r'.*ing$', 'VBG'),                 #gerund
            (r'.*ed$', 'VBD'),                  #simple past tense suffix
            (r'.*es$', 'VBZ'),                  #third person verbal suffix
            (r'.*ould$', 'MD'),                 #modal
            (r'.*\'s$', 'NN$'),                 #possessive marking
            (r'.*s$', 'NNS'),                   #common plural marker           
            (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),    #cardinal numbers
            (r'.*', 'NN')]                      #defaul tagger
regexp_tagger= nltk.RegexpTagger(patterns)
brown_tagged_sents= brown.tagged_sents(categories='fiction')
regexp_tagger= nltk.RegexpTagger(patterns)
regexp_tagger.evaluate(brown_tagged_sents)
0.3235749328349492





#########
# Problem 4:
#{<DT|PRP$|POS>?((<JJ>)|(<RB><VBN>)|(<RB><JJ>))?<VBG>?((<NNP><CC><NNP>)|(<NN>+<NNS>)|(<NNP><NN>)|(<NNP>+)|(<NN>+)|(<NNS>))}
# Precision: 69.58% Recall: 64.40 F-score:66.89
# An error my parser made was that it counted two NN's together as one NP when in some cases
# They were actually two NP's. To fix this I could put the <NN> earlier in my code, but this would
# cause other errors to occur in my code. Then, another error that came up with my parser was that the word Chancellor
# was considered an NP, while in the program it is not considered an NP. I could get rid of the NNP part of my code, but this
# would decrese my f-score. 

#########
# Problem 5:
TP = 511
FP = 83
FN = 302
TN = 2508
Recall =TP/(TP+FN)
Precision = TP/ (TP + FP)
Fscore = (2*Precision*Recall)/(Precision+Recall)
Recall = 0.6285362853628537
Precision =0.8602693602693603
Fscore=0.72636815920398

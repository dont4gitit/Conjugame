#!/usr/bin/python
# python  ReadCGFileBigDict.py

BigDict = {}   
f = open('ConjugeOutput_FalarComerPartir.txt','r')
lastlineofverb = False

for line in f.readlines():
    tenseline = line.split(':')
    if tenseline[0] == 'IS':
        partlist = []
    elif tenseline[0] == 'FN':
        infinitive = tenseline[1]
    elif tenseline[0] == 'EI':
        lastlineofverb = True

    tenseline = tenseline[1:]

    for word in tenseline:
       word = word.rstrip()
       if word not in partlist:
           partlist.append(word)

    if lastlineofverb:
        BigDict [infinitive] = partlist
        lastlineofverb = False

f.close()

for key in BigDict:
    print '\n'
    print key,
    print 'Unique words: ' + str(len(BigDict[key])) 
    print '------------------------------'
    for word in BigDict[key]:
        print word,

'''
To store a dictionary
in a file, for instance, we pickle it directly:
>>> F = open('datafile.txt', 'w')
>>> import pickle
>>> pickle.dump(D, F) # Pickle any object to file
>>> F.close( )
Then, to get the dictionary back later, we simply use pickle again to recreate it:
>>> F = open('datafile.txt')
>>> E = pickle.load(F) # Load any object from file
>>> E
{'a': 1, 'b': 2}
'''


#!/usr/bin/python
# python  ReadCGFile.py

BigList = []    # list of VerbDict's
f = open('cg-out.txt','r')
lastlineofverb = False
partlist = []

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
        VerbDict =  {'infinitive': infinitive,'partlist':partlist}
        BigList.append(VerbDict)
        lastlineofverb = False

f.close()

for verb in BigList:
    print 'Infinitive: ' + verb['infinitive']
    print '-' * (len(verb['infinitive']) + 12)
    for word in verb['partlist']:
        print word,
    print '\n'
    print 'Unique words: ' + str(len(verb['partlist'])) + '\n'


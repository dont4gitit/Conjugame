# -*- coding: latin1 -*-
#  cp860 	860, IBM860 	Portuguese
#   python   cg-01.py     cg-in.txt    cg-out.txt
from subprocess import *
output_raw = Popen(['conjugue', 'cg-in.txt'], stdout=PIPE).communicate()[0]
s = output_clipped = output_raw[(output_raw.find('#')):-2]
print (s)
s = s.decode('utf-8')
print (s)

#f = open('cg-out.txt', 'w') 
#f.write(output_clipped)  
#f.close()  

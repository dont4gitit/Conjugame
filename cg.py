# -*- coding: latin1 -*-
#   python   cg.py     Kate-F5 to reload    cg-in.txt    cg-out.txt
# file:///usr/share/doc/python2.6/html/library/subprocess.html#module-subprocess
from subprocess import *
output = Popen(['conjugue', 'cg-in.txt'], stdout=PIPE).communicate()[0]
f = open('cg-out.txt', 'w')
f.write(output)
f.close()
















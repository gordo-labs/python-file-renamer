import os
from os.path import join

print 'Rename every file name under the selected path'
dir = raw_input("Put your path: ")
addbefore = raw_input('element to add before the actual name: ')
addlast = raw_input('element to add after the actual name: ')

for root, dirs, files in os.walk(dir):
    for name in files:
        newname = str(addbefore) + name + str(addlast)
        os.rename(join(root,name),join(root,newname))

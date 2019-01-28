#!/usr/bin/env python3

myFile = open('file_005.txt', 'w')
myFile.write('abc123')
myFile.write('def456\n')
myFile.write('ghi789\n')
myFile.close()

#myFile = open('file_005.txt', 'w')
myFile = open('file_005.txt', 'a+')
myFile.write('xyz123\n')
#myFile.close()
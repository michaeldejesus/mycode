#!/usr/bin/env python3

def mapMe():
    latitude=('41.881832 degress North')
    longtiude=('-87.6298 degress West')

    return [latitude, longtiude]


print('The geo-coordinates for Chicago are: ')
myLocation=mapMe()

print("What does mapMe return??? A list or a tuple?")
print("...A list is formatted with square brackets [1,2,3]")
print("...A tuple is formatted with parentheses (1,2,3)")
print("myLocation is: ", myLocation)
print("")
print('My Latitude is: ' + str(myLocation[0]))
print('My Longitude is: ' +str(myLocation[1]))

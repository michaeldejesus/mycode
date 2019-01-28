#!/usr/bin/env python3

chicago_zoo_tuple=('Kangaroo', 'Leopard', 'Moose', 'Polar Bear', 'Bobcat')
sandiego_zoo_tuple=('Kangaroo', 'Lion', 'Grizzly Bear', 'Wildcat', 'Antelope')

print('TUPLES...')
print('Chicago Zoo: ', chicago_zoo_tuple)
print('San Diego Zoo: ', sandiego_zoo_tuple)
print()


a1, a2, a3, a4, a5=sandiego_zoo_tuple
b1, b2, b3, b4, b5=chicago_zoo_tuple

print("LOOKING at the San Diego Zoo...")
print("Animal 1:",a1)
print("Animal 2:",a2)
print("Animal 3:",a3)
print("Animal 4:",a4)
print("Animal 5:",a5)
print()
print("LOOKING at the Chicago Zoo...")
print("Animal 1:",b1)
print("Animal 2:",b2)
print("Animal 3:",b3)
print("Animal 4:",b4)
print("Animal 5:",b5)

print()
print('San Diego Zoo Tuple Length: ',len(sandiego_zoo_tuple))
print()
print('Chicago Zoo Tuple Length: ',len(chicago_zoo_tuple))




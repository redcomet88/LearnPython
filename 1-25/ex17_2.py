from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#indata = open(from_file).read()

input()

#out_file = open(to_file, 'w')
open(to_file, 'w').write(open(from_file).read())

print("Allright, all done.")

#out_file.close()
#in_file.close()
# coping one file to another in one line of code
open(input("to_file: "), 'w').write(open(input("from_file: ")).read())



#from sys import argv
#from os.path import exists

#script, from_file, to_file = argv

#print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
#indata = open(input("from_file: ")).read()
#open(input("to_file: "), 'w').write(indata)
#print(">>> in_file= ", repr(in_file))


#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit Return to continue, CTRL-C to abort.")

#input('> ')

#out_file = open(to_file, 'w')



##print("Alright, all done.")

#out_file.close()
#in_file.close()


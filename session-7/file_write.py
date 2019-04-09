# example of reading and writting in a file located in our local file system

NAME = "mynotes.txt"

# open the file
myfile = open(NAME, 'r')  # myfile is an object!!


print("file opened: {}".format(myfile.name))

contents = myfile.read()

print("the file contents are: {}".format(contents))

myfile.close()

f = open(NAME, 'a')
f.write("text example ...")
f.close()
print("THE END")

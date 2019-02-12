# example of reading a file located in our local file system

NAME = "my-notes"

# open the file
myfile = open(NAME, 'r')  # myfile is an object!!


print("file opened: {}".format(myfile.name))

contents = myfile.read()

print("the file contents are: {}".format(contents))

myfile.close()

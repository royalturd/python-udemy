f = open("demo.txt", "a")                                       # creates a file name demo.txt
f.write("Go and get a life......... (cries in corner)  ")       # writes to that file
f.close()                                                       # close the file

## to read the file in terminal ##

f = open("demo.txt", "r")                                       # r to make the file readable 
print(f.read())
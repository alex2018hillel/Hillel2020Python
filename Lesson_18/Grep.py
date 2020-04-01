def grep(pattern):
    print("Looking for {!r}".format(pattern))
    while True:
        line = yield
        if pattern in line:
            print(line)

gen = grep("got some!")
print(next(gen))
# Looking for 'got some!'
# None
print(gen.send("This line doesn't have what we are looking for"))
# None
print(gen.send("This one does. got some!"))
# This one does. got some!
# None
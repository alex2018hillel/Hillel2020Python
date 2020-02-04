def average_rating(name):
    """Create dictionary from list and calculate average rating student"""
    d = {}
    for i in l:
        a, *b = i
        d.update({a : b})
    print(d)
    for key, value in d.items():
        if key == name:
            return int(sum(value)/len(value))

l = [["Krishna", 67, 68, 69], ["Arjun", 70, 98, 63], ["Malika", 52, 56, 60]]
name = input("Input name: ")
print(average_rating(name))

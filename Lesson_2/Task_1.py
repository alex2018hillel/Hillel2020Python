import numpy as np

def frequcy(sting):
    """Count letters in string"""
    frequency = dict(zip(*np.unique(list(sting), return_counts=True)))
    for key, value in frequency.items():
        if key != " ":
            print(key + " - " + str(value))
    return frequency

sting = "spam and eggs or eggs with spam"
print(frequcy(sting))

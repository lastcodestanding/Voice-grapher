import numpy as np
import recognition as rec
import matplotlib.pyplot as plt
# create the recognizer

print("What would you like to plot?")
rec.rec()
f = open("my_result.txt", "r")
result = (f.read())
print("You said:", result)

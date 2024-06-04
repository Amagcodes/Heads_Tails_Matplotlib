#coin flip graph using matplotlib
import matplotlib.pyplot as plt
import random

#index zero = heads, index one = tails
ops = [0,0]
num = int(input("Enter a number:"))

for x in range(num):
    ops[random.randint(0,1)] +=1
    plt.bar(("Heads", "Tails"), ops, color=("red", "blue"))
    plt.pause(0.001)
    
plt.show()

input("Press any key to exit")

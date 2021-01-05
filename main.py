# coding=utf-8
import numpy as np
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput
       break
k=inputNumber("Entrez une taille de matrice (k)");
k = 2**k

a = []
b = []
for i in range(k):
    a.append(np.random.randint(-9,9,k))
    b.append(np.random.randint(-9,9,k))

a = np.array(a);
b = np.array(b);
print(a)
print(b)
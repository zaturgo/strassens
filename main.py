# coding=utf-8
import numpy as np
import time

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Veuillez entrer un entier")
       continue
    else:
       return userInput
       break
k=inputNumber("Entrez une taille de matrice (2^k)");
k = 2**k
a = []
b = []
for i in range(k):
    a.append(np.random.randint(-9,9,k))
    b.append(np.random.randint(-9,9,k))

a = np.array(a);
b = np.array(b);
start = time.perf_counter()
end = time.perf_counter()
print(f"L'exécution a pris {end - start:0.4f} secondes")

# coding=utf-8
import numpy as np
import time
def classic(a,b,c,dim):
    for i in range(dim):
        for j in range(dim):
            c[i][j] = 0
            for k in range(dim):
                c[i][j] += a[i][k]*b[k][j]
    return c;
timeClassic = 0
timeStrassen = 1
k = 0;
while timeClassic<timeStrassen:
    k = k+1
    print("--------------------------")
    print("Execution pour matrice de taille "+str(2**k)+" (k="+str(k)+")")
    a = []
    b = []
    c = []
    for i in range(2**k):
        a.append(np.random.randint(-9,9,2**k))
        b.append(np.random.randint(-9,9,2**k))
        c.append(np.random.randint(-9,9,2**k))
    a = np.array(a);
    b = np.array(b);
    c = np.array(b);
    start = time.perf_counter()
    classic(a,b,c,2**k)
    end = time.perf_counter()
    print(f"L'exécution classique a pris {end - start:0.6f} secondes")
    timeClassic = end - start
    #start = time.perf_counter()
    #strassen(a,b)
    #end = time.perf_counter()
    #print(f"L'exécution de strassen a pris {end - start:0.4f} secondes")
    #timeStrassen = end - start
    timeStrassen = timeClassic-1
print("----------------------------")
print("Strassen est plus rapide à partir de k="+str(k))


# coding=utf-8
import numpy as np
import time

def strassen(a, b):
	# Si matrice de taille 1, on multiplie a*b
	if len(a) == 1:
		return a * b

    # Découpe les matrices
	rowA, colA = a.shape
	rowB, colB = b.shape
	a11, a12, a21, a22 = a[:rowA//2, :colA//2], a[:rowA//2, colA//2:], a[rowA//2:, :colA//2], a[rowA//2:, colA//2:]
	b11, b12, b21, b22 = b[:rowB//2, :colB//2], b[:rowB//2, colB//2:], b[rowB//2:, :colB//2], b[rowB//2:, colB//2:]

	# Strassen
	q1 = strassen(a11 - a12, b22)
	q2 = strassen(a21 - a22, b11)
	q3 = strassen(a22, b11 + b21)
	q4 = strassen(a11, b12 + b22)
	q5 = strassen(a11 + a22, b22 - b11)
	q6 = strassen(a11 + a21, b11 + b12)
	q7 = strassen(a12 + a22, b21 + b22)

	# Calcul nouvelle matrice
	c11 = q1 - q3 - q5 + q7
	c12 = q4 - q1
	c21 = q2 + q3
	c22 = - q2 - q4 + q5 + q6

	return np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

def classic(a,b,c,dim):
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                c[i][j] += a[i][k]*b[k][j]
    return c;

timeClassic = 1
timeStrassen = 0
k = 0;
while timeClassic > timeStrassen:
    k = k+1
    print("--------------------------")
    print("Execution pour matrice de taille "+str(2**k)+" (k="+str(k)+")")
    a = []
    b = []
    c = []
    for i in range(2**k):
        a.append(np.random.randint(-9,9,2**k))
        b.append(np.random.randint(-9,9,2**k))
        c.append(np.zeros(2**k))
    a = np.array(a)
    b = np.array(b)
    c = np.array(b)
    start = time.perf_counter()
    classic(a,b,c,2**k)
    end = time.perf_counter()
    print(f"L'exécution classique a pris {end - start:0.6f} secondes")
    timeClassic = end - start
    start = time.perf_counter()
    strassen(a,b)
    end = time.perf_counter()
    print(f"L'exécution de strassen a pris {end - start:0.6f} secondes")
    timeStrassen = end - start
    timeStrassen = timeClassic-1
print("----------------------------")
print("Strassen est plus rapide à partir de k="+str(k)+" (matrice de taille "+str(2**k)+")")


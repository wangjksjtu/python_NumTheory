from NumTheory import *

times = 0
for i in range(10):
    n = EulerPseudoprime(5, 0.0001)
    print n
    if isPrime(n[0]):
        #print n
        times += 1
print (times/10.0)

print Legendre(137, 227)
print Legendre(2, 17)
print Jacobi(286, 563)

n = FermatPseudoprime(60, 0.00000001)[0]
print n
print isPrime(n)
print isPrime(2 ** 128 + 1)


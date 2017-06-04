## python_NumTheory
A python library that realizes the basic algorthims in number theory

### Functions ###
    def isPrime(n): # judge if a positive integer is a prime
    def countPrime(a, b, c = 1): # count number of primes in [a, b], c is interval
    def getAllPrime(a, b, c = 1): # get all primes in [a, b], c is interval
    def getResidue(n, mode = 0): # get residue of a positive integer
    def EuclidDivision(a, b, mode = 0): # finish euclid division
    def greatestCommonDivisor(a, b): # get the greatest common divisor of two integers
    def greatestCommonDivisor_n(a): # get the greatest common divisor of n integers (a is a list)
    def leastCommonMultiple(a, b): # get the least common multiple of two integers
    def leastCommonMultiple_n(a): # get the least common multiple of n integers (a is a list)
    def isCoprime(a, b): # judge if a and b are coprime
    def getReciprocal(a, m) # get reciprocal of a mod m
    def decompose(a): # decompose an integer in violence
    def getStandardDecomposition(a): # get standard decomposition expression in violence
    def Bezout(a, b): # Bezout theory
    def binaryLinearDiophantineEquation(a, b, c): # get answer of binary linear diophantine equation
    def quickPow(a, b, m): # quick pow implementaion
    def quadraticResidue_prime(p): # get quadratic residues of a prime
    def quadraticNonResidue_prime(p): # get quadratic non-residues of a prime
    def quadraticResidue_prime_pair(p): # get quadratic residue-pair of a prime
    def EllipticCurveEquation(a, b, c, d, p): # solve elliptic curve equation
    def Legendre(a, p): # caculate Legendre symbol
    def Jacobi(a, p): # caculate Jacobi symbol
    def NaiveModSquareEquation(a, m): # solve mod-square equation in violence
    def ModSquareEquation(a, m): # solve mod-square equation
    def NaiveSquarePEquation(p): # solve square p equation in violence
    def EulerFunction(m): # implement euler function
    def getSimplifySurplus(m): # get simplify surplus set of m
    def isPrimaryRoot(g, p): # judge if g is primary root of p 
    def getAllPrimaryRoot_naive(p): # get all primary root in violence
    def getAllPrimaryRoot(p): # get all primary root
    def FermatPseudoprime(size, probability = 0.0001): # generate Fermat pseudoprime
    def EulerPseudoprime(size, probability = 0.0001): # generate Euler pseudoprime
    
### Attentions ###
+ There are not user friendly documents now.
+ There are still some alogorithms unfinished.
+ I will update this repo if I have free time and I think it's worth doing so. 

### Later Work ###
+ def SquarePEquation(p):
+ def Even_fractions(x):
+ def getAllPrimaryRoot_n(p, a):
+ related useful functions
+ other algorithms such as RSA.

### Contact me ###
+ wangjksjtu_01@sjtu.edu.cn
+ 249446879@qq.com

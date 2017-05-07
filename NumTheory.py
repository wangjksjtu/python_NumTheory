# This is a function-file which is related to the common algorithms in number theory.
# Date: 2017-05-04

def isPrime(n):
    if (n < 2 or type(n) != type(1)): return False
    if (n == 2):
        return True
    else:
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return False
    return True

def countPrime(a, b, c = 1): #[a, b) and c is interval
    count = 0
    for x in range(a, b, c):
        if isPrime(x):
            count += 1
    return count

def getAllPrime(a, b, c = 1): # [a, b) and c is interval
    prime_list = []
    for x in range(a, b, c):
        if isPrime(x):
            prime_list.append(x)
    return prime_list

def getResidue(n, mode = 0):
    # mode:  0: 'Smallest Non-Negtive'
    #        1: 'Largest Non-Positive'
    #        2: 'Absolute Minimum' (other modes except 0 and 1)
    if mode == 0:
        return range(0, n)
    elif mode == 1:
        return range(-n + 1, 0 + 1)
    else:
        if (n % 2 == 0):
            return [range(-n/2, n/2), range(-n/2 + 1, n/2 + 1)]
        else:
            return range(-(n - 1)/2, (n - 1)/2 + 1)

def EuclidDivision(a, b, mode = 0):
    # mode:  0: 'Smallest Non-Negtive'
    #        1: 'Largest Non-Positive'
    #        2: 'Absolute Minimum' (other modes except 0 and 1)
    if mode == 0:
        return (a / b, a % b)
    elif mode == 1:
        if a % b == 0:
            return (a / b, a % b)
        else:
            return (a / b + 1, a % b - b)
    else:
        if (b % 2 == 1):
            if (a % b) <= (b - 1)/2:
                return (a / b, a % b)
            else:
                return (a / b + 1, a % b - b)
        else:
            if (a % b == b / 2):
                return [(a / b, a % b), (a / b + 1, a % b - b)]
            else:
                return (a / b, a % b)

def greatestCommonDivisor(a, b):
    a, b = abs(a), abs(b)
    if (a < b): a, b = b, a
    while (True):
        r = a % b
        a, b = b , r
        if (r == 0): break
    return a

def isCoprime(a, b):
    if (greatestCommonDivisor(a, b) == 1):
        return True
    return False

def decompose(a):
    if a == 0: return 0
    a = abs(a)
    plist = []
    alphalist = []
    flag = False
    while (True):
        for x in range (2, int(a ** 0.5) + 1):
            if a % x == 0:
                plist.append(x)
                alphalist.append(0)
                break
            if (x == int(a ** 0.5)):
                plist.append(a)
                alphalist.append(1)
                flag = True
        if (flag or a == 1): break
        while (a % x == 0):
            a /= x
            alphalist[-1] += 1
    return plist, alphalist

def getStandardDecomposition(a):
    if a == 0: return "0"
    plist, alphalist = decompose(a)
    if (a < 0):
        string = '-'
    else: string = ''
    for i, p in enumerate(plist):
        if (i != 0):
            string += "*"
        string += str(p)
        if alphalist[i] != 1:
            string += "^" + str(alphalist[i])
    return string

def quickPow(a, b, m):
    if (b == 1):
        return a % m
    else:
        if (b % 2 == 0):
            x = quickPow(a, b / 2, m)
            return x * x % m
        else:
            x = quickPow(a, (b - 1)/ 2, m)
            return x * x * a % m

def quadraticResidue_prime(p):
    if isPrime(p):
        if p == 2: return [1,]
        else:
            alist = []
            for x in range(1, (p - 1)/2 + 1):
                alist.append(x ** 2 % p)
            alist.sort()
            return alist
    else: return False

def quadraticNonResidue_prime(p):
    alist = list(set(range(1,p)) - set(quadraticResidue_prime(p)))
    alist.sort()
    return alist

def quadraticResidue_prime_pair(p):
    if isPrime(p):
        if p == 2: return [1,]
        else:
            alist = []
            for x in range(1, (p - 1)/2 + 1):
                alist.append(((x ** 2 % p), x))
            alist.sort()
            return alist
    else:
        return False

def EllipticCurveEquation(a, b, c, d, p):
    results = []
    if not isPrime(p): return False
    def f(x):
        return a * x ** 3 + b * x ** 2 + c * x + d
    alist = quadraticResidue_prime(p)
    blist = quadraticResidue_prime_pair(p)
    for x in range(0, p):
        if (f(x) % p) in alist:
            y = blist[alist.index(f(x) % p)][1]
            results.append((x, y))
            results.append((x, p-y))
        else:
            if f(x) % p == 0:
                results.append((x, 0))
    return results

def Legendre(a, p):
    if not isPrime(p):
        return False
    if (p == 2):
        return 1
    a = a % p
    if isPrime(a):
        if a % 2 == 1:
            return (-1) ** ((p - 1) / 2 * (a - 1) / 2) * Legendre(p, a)
        else:
            if (p % 8 == 1 or p % 8 == 7): return 1
            else: return -1
    else:
        plist, alphalist = decompose(a)
        plist2 = []
        for i, x in enumerate(alphalist):
            if (x % 2 != 0):
                plist2.append(plist[i])
        result = 1
        for i in range(len(plist2)):
            result *= Legendre(plist2[i], p)
        return result

def Jacobi(a, p):
    a = a % p
    plist, alphalist = decompose(p)
    plist2 = []
    for i, x in enumerate(alphalist):
        if (x % 2 != 0):
            plist2.append(plist[i])
    result = 1
    for i in range(len(plist2)):
        result *= Legendre(a, plist2[i])
    return result

def NaiveModEquation(a, m):
    for x in range(0, m):
        if x**2 % m == a:
            return (x, m - x)

def NaiveSquarePEquation(p):
    for x in range(0, int(p ** 0.5) + 1):
        y = p - x ** 2
        if ((int(y ** 0.5) ** 2 == y) or ((int(y ** 0.5) + 1) ** 2 == y)
                or ((int(y ** 0.5) - 1) ** 2 == y)):
            return (x, int(y ** 0.5))
    return False

def EulerFunction(m):
    plist, aplhalist = decompose(m)
    result = m
    for x in range(len(plist)):
        result *= plist[x] - 1
        result /= plist[x]
    return result

def getSimplifySurplus(m):
    result = []
    for x in range(1, m):
        if isCoprime(x, m):
            result.append(x)
    return result

def isPrimaryRoot(g, p):
    if not isPrime(p) or g <= 1:
        return False
    plist, alphalist = decompose(p - 1)
    for i in range(len(plist)):
        if (g ** ((p - 1)/plist[i]) % p == 1):
            return False
    return True

def getAllPrimaryRoot_naive(p):
    if not isPrime(p):
        return False
    alist = []
    for x in range(1, p):
        if isPrimaryRoot(x, p):
            alist.append(x)
    return alist


def getAllPrimaryRoot(p):
    if not isPrime(p):
        return False
    g = 0
    for x in range(2, p):
        if isPrimaryRoot(x, p):
            g = x
            break;
    alist = getSimplifySurplus(p - 1)
    result = []
    for x in alist:
        result.append(quickPow(g,x,p))
    result.sort()
    return result

def main():
#########################################
#   Test of isPrime
    print isPrime(9)
    print isPrime(2017)
    print isPrime(2**(2**4) + 1)
    print isPrime(5098129)
#########################################
#   Test of countPrime
    print countPrime(2, 100)
    print countPrime(2, 3)
#########################################
#   Test of getAllPrime
    print getAllPrime(2, 100)
    print len(getAllPrime(2, 10000))
#########################################
#   Test of getResidue
    print getResidue(13)
    print getResidue(13, 1)
    print getResidue(13, 2)
    print getResidue(14, 2)
#########################################
#   Test of EuclidDivision
    print EuclidDivision(1247894560, 132131)
    print EuclidDivision(28, 11, 0)
    print EuclidDivision(28, 11, 1)
    print EuclidDivision(30, 12, 2)
    print EuclidDivision(29, 12, 2)
#########################################
#   Test of greatestCommonDivisor
    print greatestCommonDivisor(- 2007 * 5 * 7, 2007 * 3 * 5)
#########################################
#   Test of isCoprime
    print isCoprime(2017, 2017 * 456)
    print isCoprime(2017, 2 ** (2 ** 4) + 1)
#########################################
#   Test of decompose
    print decompose(2**10)
    print decompose(45623156421)
    print decompose(2**10*3**10*7**5)
    print decompose(0)
    print decompose(2017)
#########################################
#   Test of getStandardDecomposition
    print getStandardDecomposition(-2**10*3**10*7**5)
    print getStandardDecomposition(2017 * 2014)
#########################################
#   Test of quadraticResidue_prime
    print quadraticResidue_prime(17)
    print quadraticNonResidue_prime(17)
    print quadraticResidue_prime_pair(17)
#########################################
#   Test of ECC_Equation
    print EllipticCurveEquation(1,0,1,1,7)
    print EllipticCurveEquation(1,0,2,-1,7)
    print EllipticCurveEquation(1,0,3,-1,7)
#########################################
#   Test of Legendre
    print Legendre(2, 59)
    print Legendre(5, 41)
    print Legendre(37, 79)
    print Legendre(5, 2017)
    print Legendre(-1, 41)
#########################################
#   Test of Jacobi
    print Jacobi(286, 563)
    print Jacobi(191, 397)
#########################################
#   Test of NaiveModEquation
    print NaiveModEquation(39, 105)
    print NaiveModEquation(1369, 2310)
#########################################
#   Test of NaiveSquareQEquation
    print NaiveSquarePEquation(797)
    print NaiveSquarePEquation(100000037)
#########################################
#   Test of EulerFunction
    print EulerFunction(2048)
    print EulerFunction(40)
#########################################
#   Test of isPrimaryRoot
    print isPrimaryRoot(35, 41)
    print isPrimaryRoot(32, 41)
    print isPrimaryRoot(1, 41)
#########################################
#   Test of getAllPrimaryRoot_naive
    print getAllPrimaryRoot_naive(41)
    print getAllPrimaryRoot_naive(43)
#########################################
#   Test of getSimplifySurplus
    print getSimplifySurplus(40)
#########################################
#   Test of getAllPrimaryRoot
    print getAllPrimaryRoot(41)
    print getAllPrimaryRoot(43)
#########################################
#   Test of quickPow
    print quickPow(6, 39, 41)
if __name__ == "__main__":
    main()

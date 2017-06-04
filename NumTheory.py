# This is a function-file which is related to the common algorithms in number theory.
# Date1: 2017-05-04
# Date2: 2017-05-10
# Date3: 2017-05-18
import random

def isPrime(n):
    if (n < 2 or (type(n) != type(1) and type(n) != type(1L))):
        return False
    if (n == 2):
        return True
    else:
        for x in xrange(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return False
    return True

def countPrime(a, b, c = 1): #[a, b) and c is interval
    count = 0
    for x in xrange(a, b, c):
        if isPrime(x):
            count += 1
    return count

def getAllPrime(a, b, c = 1): # [a, b) and c is interval
    prime_list = []
    for x in xrange(a, b, c):
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

def greatestCommonDivisor_n(a):
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return greatestCommonDivisor(a[0], a[1])
    else:
        b1 = a[0]
        b2 = a[1]
        c = greatestCommonDivisor(b1, b2)
        d = [c,] +  a[2:]
        return greatestCommonDivisor_n(d)

def leastCommonMultiple(a, b):
    return abs(a * b) / greatestCommonDivisor(a, b)

def leastCommonMultiple_n(a):
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return leastCommonMultiple(a[0], a[1])
    else:
        b1 = a[0]
        b2 = a[1]
        c = leastCommonMultiple(b1, b2)
        d = [c, ] + a[2:]
        return leastCommonMultiple_n(d)

def isCoprime(a, b):
    if (greatestCommonDivisor(a, b) == 1):
        return True
    return False

def getReciprocal(a, m):
    if (isCoprime(a, m)):
        for i in xrange(1, m):
            if a * i % m == 1:
                return i
    else:
        return False

def decompose(a):
    if a == 0 or a == 1: return a
    a = abs(a)
    plist = []
    alphalist = []
    flag = False
    #if (a == 2 or a == 3):
    #    return ([a,], [1,])
    while (True):
        if a == 2 or a == 3:
            plist.append(a)
            alphalist.append(1)
            break
        for x in range (2, int(a ** 0.5) + 1):
            if a % x == 0:
                plist.append(x)
                alphalist.append(0)
                break
            if (x == int(a ** 0.5)):
                plist.append(a)
                alphalist.append(1)
                flag = True
        #print plist, alphalist
        if (flag or a == 1): break
        #print a, x
        while (a % x == 0):
            a /= x
            #print a, x
            alphalist[-1] += 1
        #print a, x
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

def Bezout(a, b):
    (r1, r2) = (a, b)
    (s1, s2) = (1, 0)
    (t1, t2) = (0, 1)
    while (r2 != 0):
        q = r1 / r2
        r1 = r1 % r2
        (r1, r2) = (r2, r1)
        if (r2 == 0): break
        s1 = s2 * (-q) + s1
        (s1, s2) = (s2, s1)
        t1 = t2 * (-q) + t1
        (t1, t2) = (t2, t1)
    return (s2, t2)

def binaryLinearDiophantineEquation(a, b, c):
    d = greatestCommonDivisor(a, b)
    if (c % d != 0):
        return False
    else:
        a /= d
        b /= d
        c /= d
        x0, y0 = d * Bezout(a, b)
        return [(x0, y0), "x = " + str(x0) + " - " + str(b) + " * t",
                "y = " + str(y0) + " + " + str(a)  + " * t"]

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
            for x in xrange(1, (p - 1)/2 + 1):
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
            for x in xrange(1, (p - 1)/2 + 1):
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
    for x in xrange(0, p):
        if (f(x) % p) in alist:
            y = blist[alist.index(f(x) % p)][1]
            results.append((x, y))
            results.append((x, p-y))
        else:
            if f(x) % p == 0:
                results.append((x, 0))
    return results

def Legendre(a, p):
    a = a % p
    if not isPrime(p):
        return False
    if (p == 2):
        return 1
    if a == 1: return 1
    if a == p - 1: return (-1) ** ((p - 1)/2)
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
        for i in xrange(len(plist2)):
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
    for i in xrange(len(plist2)):
        result *= Legendre(a, plist2[i])
    return result

def NaiveModSquareEquation(a, m):
    result = []
    for x in xrange(0, int(m ** 0.5) + 1):
        if x**2 % m == a:
            result.append((x, m - x))
    if (len(result) == 0):
        return False
    else: return result

def ModSquareEquation(a, m):
    pass

def NaiveSquarePEquation(p):
    for x in xrange(0, int(p ** 0.5) + 1):
        y = p - x ** 2
        if ((int(y ** 0.5) ** 2 == y) or ((int(y ** 0.5) + 1) ** 2 == y)
                or ((int(y ** 0.5) - 1) ** 2 == y)):
            return (x, int(y ** 0.5))
    return False

def EulerFunction(m):
    plist, aplhalist = decompose(m)
    result = m
    for x in xrange(len(plist)):
        result *= plist[x] - 1
        result /= plist[x]
    return result

def getSimplifySurplus(m):
    result = []
    for x in xrange(1, m):
        if isCoprime(x, m):
            result.append(x)
    return result

def isPrimaryRoot(g, p):
    if not isPrime(p) or g <= 1:
        return False
    plist, alphalist = decompose(p - 1)
    for i in xrange(len(plist)):
        if (g ** ((p - 1)/plist[i]) % p == 1):
            return False
    return True

def getAllPrimaryRoot_naive(p):
    if not isPrime(p):
        return False
    alist = []
    for x in xrange(1, p):
        if isPrimaryRoot(x, p):
            alist.append(x)
    return alist

def getAllPrimaryRoot(p):
    if not isPrime(p):
        return False
    g = 0
    for x in xrange(2, p):
        if isPrimaryRoot(x, p):
            g = x
            break;
    alist = getSimplifySurplus(p - 1)
    result = []
    for x in alist:
        result.append(quickPow(g,x,p))
    result.sort()
    return result

def FermatPseudoprime(size, probability = 0.0001):
    # Without consideration of Carmichael Number
    # If one integer is Carmichael Number, the pro is non-sense
    times = 0
    if (size <= 2): return False
    while (True):
        pro = 1
        if (times > 2 ** (size - 1)):
            size += 1
            times = 0
        n = random.randint(2**(size - 1), 2**size - 1)
        #print n
        if n % 2 == 0: continue
        while (pro > probability):
            b = random.randint(2, n - 2)
            times2 = 0
            while not (isCoprime(n, b)):
                b = random.randint(2, n - 2)
                times2 += 1
                if times2 >= n:
                    break
            if (times2 >= n):
                break
            if (quickPow(b, n - 1, n) != 1):
                break
            else:
                pro *= 0.5
        if (pro <= probability):
            return n, len(bin(n)) - 2
        times += 1

# This function may have some bug remaining to fix
# This is because that this function has low efficiency and can not
# proper specific digit eulerpseudoprime (always produce larger ones)
def EulerPseudoprime(size, probability = 0.0001):
    times = 0
    if (size <= 2): return False
    while (True):
        pro = 1
        if (times > 2 ** (size - 1)):
            times = 0
            size += 1
        n = random.randint(2 ** (size - 1), 2**size - 1)
        if (n % 2 == 0):
            continue
        while (pro > probability):
            b = random.randint(2, n - 2)
            times2 = 0
            '''while not (isCoprime(n, b)):
                b = random.randint(2, n - 2)
                times2 += 1
                if times2 >= n:
                    break
            if times2 >= n:
                break '''
            r = quickPow(b, (n - 1)/2, n)
            if (r != 1 and r != r - 1):
                break
            #print (b, n)
            s = Jacobi(b, n)
            #print s
            if (r != s):
                #print r
                break
            pro *= 0.5
        if (pro <= probability):
            return n, len(bin(n)) - 2
        times += 1

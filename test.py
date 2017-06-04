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
#   Test of greatestCommonDivisor_n
    print greatestCommonDivisor_n([120, 150, 210, 35])
    print greatestCommonDivisor_n([-2 * 2017, 3 * 7, 7 * 2017])
#########################################
#   Test of leastCommonMultiple
    print leastCommonMultiple(2 * 2017, 3 * 2017)
#########################################
#   Test of leastCommonMultiple_n
    print leastCommonMultiple_n([120, 150, 210, 35])
    print leastCommonMultiple_n([3 * 5, 5 * 7, 7 * 11])
#########################################
#   Test of Bezout
    print Bezout(1859, 1573)
    print Bezout(46480, 39423)
#########################################
#   Test of getReciprocal
    print getReciprocal(2, 4)
    print getReciprocal(3, 7)

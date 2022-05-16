from sympy import sieve

def Summation_Of_Primes():
    sieve.extend(2000000)
    return print(sum(sieve._list))


if __name__ == '__main__':
    Summation_Of_Primes()


def Special_Pythagorean_Triplet():
    for c in range(0,1000):
        for b in range(0,1000):
            for a in range(0,1000):
                if c > b and b > a :
                    print(a,b,c )
                    if a+b+c == 1000:
                        if a*a + b*b == c*c :
                            return print(a*b*c)

if __name__ == '__main__':
    Special_Pythagorean_Triplet()

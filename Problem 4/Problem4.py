def Largest_Palindrome_Product():
    listnumbers = []
    for number1 in range(100,1000):
        for number2 in range(100,1000):
            res = number1 * number2
            list = []
            for char in str(res) :
                list.append(char)
            if list[len(list) -1 ] != 0:
                list.reverse()
                newnumber = int("".join(list))
                if newnumber == res:
                    listnumbers.append(newnumber)
    return print(max(listnumbers))

            
if __name__ == '__main__':
    Largest_Palindrome_Product()

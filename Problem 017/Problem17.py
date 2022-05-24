from num2words import num2words
def Number_Letter_Counts():
    sum = 0
    for number in range(1,1001):
        word = num2words(number)
        word = "".join(word.split("-"))
        word = "".join(word.split(" "))
        for letter in word:
            sum += 1
    return print(sum)

if __name__ == '__main__':
    Number_Letter_Counts()

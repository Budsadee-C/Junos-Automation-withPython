class numberSeries:
    def __init__(self,num):
        self.number = num

    def getStart():
        return self.number
    def SeriesNumber(self,terms,number):
        sum = 0
        init = number
        for i in range(0, terms):
            print(number, end=" ")
            sum += number
            number = (number * 10) + init
        print("Sum of above series is:", sum)

while True:
    try:
        terms= int(input ('Enter number of terms: '))
        break
    except :
        continue
while True:
    try:
        number= int(input ('Enter number: '))
        break
    except :
        continue
series = numberSeries(number)
series.SeriesNumber(terms,number)

class Personal:
   def __init__(self,user ):
       self.user = user

class BMI:
    def __init__(self,high,weight):
        self.heigh = heigh
        self.weight = weight
    def CalculateBMI(self):
        bmi = weight/(heigh*heigh)
        print(bmi)
        if bmi <= 18.5:
            return 'thin'
        elif bmi > 18.5 and bmi <= 22.90:
            return 'normal'
        elif bmi > 22.90 and bmi <= 24.90:
            return 'fat level 1'
        elif bmi > 24.90 and bmi <= 29.90:
            return 'fat level 2'
        else:
            return 'fattest'

Person = Personal(input('Please enter your name: '))
while True:
    try:
        heigh= float(input ('Enter your tall (cm): '))/100
        break
    except :
        continue
while True:
    try:
        weight= float(input ('Enter your weight(kg): '))
        break
    except :
        continue


bmi_person = BMI(heigh,weight)
print(Person.user + " ,the result of your BMI that show you are: " + str(bmi_person.CalculateBMI()))

class Formula:

    def REE(self, weight, height, age, mod):
        if mod == 5:
            ree = 10 * weight + (6.25 * height) - (5 * age) + mod

        elif mod == 161:
            ree = 10 * weight + (6.25 * height) - (5 * age) - mod
        return ree

    def calcTDEE(self, ree, activity):
        if activity == 1:
            TDEE = ree * 1.2
        elif activity == 2:
            TDEE = ree * 1.375
        elif activity == 3:
            TDEE = ree * 1.55
        elif activity == 4:
            TDEE = ree * 1.725
        else:
            print("Incorrect Input!")
        return TDEE

    def weightTDEE(self, goal, tdee):
        if goal == 1:
            newTDEE = tdee - (tdee * 0.20)
        elif goal == 2:
            newTDEE = tdee + (tdee * 0.20)
        return newTDEE


class Macros:

    def returnLbs(self, weight):
        lbs = weight * 2.2
        return lbs

    def returnKG(self, weight):
        kg = weight / 2.2
        return kg


class User:

    def getDetails(self):
        print("Please input your gender\nM for male and F for female")
        gender = input()
        if gender == 'M' or gender == 'm':
            mod = 5
        elif gender == 'F' or gender == 'f':
            mod = 161
        else:
            print("That is an incorrect input\nTry again...")

        print("Please input your weight in KG")
        weight = int(input())
        print("Please input you height")
        height = int(input())
        print("Please input your age")
        age = int(input())

        # Instantiates and object of formula to return Resting Energy Expenditure (GetREE) and Calculate Total Daily
        # Energy Expenditure
        f = Formula()
        getREE = f.REE(weight, height, age, mod)
        print("How active are you\nA: Sedentary\n2: Light Active\n3: Moderately Active\n4: Very Active")
        activity = int(input())
        getTDEE = f.calcTDEE(getREE, activity)
        print("What are your weight management goals?\n1: Weight Loss\n2: Weight Gain")
        goal = int(input())
        modTDEE = f.weightTDEE(goal, getTDEE)

        # A tuple comprised of the outputs from the Formula class
        t = (getREE, getTDEE, modTDEE, weight)
        return t


print("\t\tFITPAD\t\t")
startup = User()
userDetails = startup.getDetails()
print("Your Resting Energy Expenditure is:", userDetails[0])
print("Your daily Calorie expenditure is: ", userDetails[1])
print("To reach your weight goals you must consume:", userDetails[2], "calories")


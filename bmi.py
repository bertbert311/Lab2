def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height**2)
    print("BMI is " + str(round(bmi,2)))
    if bmi < 18.5:
        print("User is underweight")
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("User is normal weight")
        return 0
    elif 25.0 < bmi:
        print("User is Over weight")
        return 1




calculate_bmi(weight=57, height=1.73)


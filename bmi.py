def calculate_bmi(height,weight):
    print("Height=",height)
    print("Weight=",weight)

    #code to calculate BMI 
    bmi = weight/(height*height)

    #code to display calculate BMI
    print("BMI=",bmi) 
    if bmi < 18.5:
        print("Underweight")    
    elif 18.5 <= bmi < 24.9:    
        print("Normal weight")
    elif bmi>29.9:
        print("Over weight")

calculate_bmi(weight=37, height=1.73)

calculate_bmi(weight=57, height=1.73)

calculate_bmi(weight=97, height=1.73)

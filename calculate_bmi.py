def calculate_bmi(height,weight): 
    print("Height", str(height))
    print("Weight", str(weight))

    #bmi calculation
    bmi = weight/(height*2)

    #output bmi
    print(f"Your bmi is {bmi:.2f}")

    
    if bmi<18.5:
        print("Under Weight")
    elif bmi<25.0 & bmi>18.5:
        print("Normal Weight") 
    elif bmi>25.0:
        print("Over Weight")
calculate_bmi(weight=57,height=1.73)
temp_list = [37, 57, 97]
def main():
    print("ET0735(DevOps for AIoT) - Lab2 - Introduction to Python")
    display_main_menu()
    temp_list = get_user_input()
    print(calc_average(temp_list))
    min_temp, max_temp = find_min_max(temp_list)
    print("Min Temperature:", min_temp)

def display_main_menu():
    print("Enter some numbers separated by commmas (e.g, 5, 67, 32)")
    


    
def calc_average():
    print("Calculate Average")


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


def get_user_input():
    inputstr = input()
    string_list =inputstr.split(",")
    float_list = [float(item.strip()) for item in string_list]
    return float_list

def calc_average(temp_list):
    return sum(temp_list)/len(temp_list)
    
def find_min_max(temp_list):
    return min(temp_list), max(temp_list)

    
def sort_temperature():
    print("sort_temperature")
def calc_median_temperature():
    print("calc_median_temperature")


calculate_bmi(weight=37, height=1.73)

calculate_bmi(weight=57, height=1.73)

calculate_bmi(weight=97, height=1.73)
if __name__=="__main__":
    main()
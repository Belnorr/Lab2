def main():
    print("ET0735 (DevOps for AIoT - Lab2 - Introduction to Python)")
    display_main_menu()


def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    input_str = input(str)
    str_list = input_str.split(",")
    print(str_list)
    return str_list

def calc_average(str_list):
    print("calc_average")
    for eachstr in str_list:
        total += total + float(each_str)
    average = float(total/str_list)
    return average
def find_min_max():
    print("find_min_max")

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

num_list = get_user_input ()
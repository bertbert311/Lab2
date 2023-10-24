import statistics
def main():
    global listofnumbers
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    sort_temperature(num_list)
    calc_median_temperature(num_list)



def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    x = input()
    y = x.split(",")
    listofnumbers = list(y)
    for i in range(0, len(listofnumbers)):
        listofnumbers[i] = float(listofnumbers[i])
    print(listofnumbers)
    return listofnumbers



def calc_average(num_list):
    z = num_list
    sumoftemp = sum(z)
    average = sumoftemp/len(z)
    return average



def find_min_max(num_list):
    z = num_list
    mintemp = min(z)
    maxtemp = max(z)
    print("Min Temperature is: " + str(mintemp))
    print("Max Temperature is: " + str(maxtemp))
    return mintemp, maxtemp

def sort_temperature(num_list):
    num_list.sort()
    print("Sorted Temperatures are: " + str(num_list))

def calc_median_temperature(num_list):

    print("Median Temperature is: " + str(statistics.median(num_list)))


if __name__ == "__main__":
    main()
def BMI(weight, height):
    return round(weight/(height**2), 2)

print(BMI(80, 1.73))

def bmi_checker(list_of_stats):
    res_string = ''
    for item in list_of_stats:
        # print(item)
        this_bmi = BMI(item[0], item[1])
        if this_bmi < 18.5:
            res_string += 'under '
        elif this_bmi >= 18.5 and this_bmi < 25.0:
            res_string += 'normal '
        elif this_bmi >= 25.0 and this_bmi < 30.0:
            res_string += 'over '
        else:
            res_string += 'obese '
    return res_string

stat_list = [[80, 1.73], [55, 1.58], [49, 1.91]]

x = input("how many sets of data are entering today?\n")
x_int = int(x)
the_list = []
for item in range(x_int):
    weight = int(input("weight: "))
    height = float(input("height: "))
    the_list.append(list([weight, height]))
# print(the_list)


print(bmi_checker(the_list))  
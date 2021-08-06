# 1
def func():
    print("Hello World!")

func()

# 2
def func1(name):
    print('Hi my name is ' + name)

func1("Doug")

# 3
def func3(x, y, z):
    if z:
        return x
    else:
        return y

# print(func3(1, 2, True))

# 4
func4 = lambda x,y : x*y
# print(func4(2,3))

# 5
def is_even(arg):
    if arg % 2 ==0:
      return True
    else:
      return False

is_even_II = lambda arg : True if arg % 2 ==0 else False

print(is_even(5))
print(is_even_II(6))

# 6
def greater_than_test(x, y):
    if x > y:
        return True
    else:
        return False

# print(greater_than_test(3,1))

# 7
def addition_of_args(*args):
    my_sum = 0
    for item in args:
        my_sum += item
    return my_sum

print(addition_of_args(1,2,7,99))

# 8
def return_even(*args):
    my_list = []
    for item in args:
        if item % 2 == 0:
            my_list.append(item)
    return my_list

print(return_even(1,2,3,8,6,7,9,11,12,44,77))

# 9
def even_to_upper(my_string):
    return_string = ''
    j = 0
    for i in my_string:
        if j % 2 == 0:
            return_string += i.upper()
        else:
            return_string += i.lower()
        j+=1
    return return_string

print(even_to_upper("TEST ThIS IS A TEST"))

# 10
def less_than(x,y):
    if x % 2 ==0 and y % 2 ==0:
        return min(x, y)
    elif x % 2 != 0 or y % 2 != 0:
        return max(x,y)

# print(less_than(2,5))

# 11
def first_letter_check(first_string, second_string):
    if first_string[0].lower() == second_string[0].lower():
        return True
    else:
        return False

print(first_letter_check("Bam", "bunch"))

# 12
# I'm a bit confused by this quesion
def other_side_of_seve(my_num):
    return my_num * 2 + 7

# 13
def first_and_fourth_cap(my_string):
    return_string = ''
    j = 0
    
    for item in my_string:
        if j == 0 or j == 3:
            return_string += item.upper()
        else:
            return_string += item

        j+=1
    return return_string
# print(first_and_fourth_cap("test string"))

     
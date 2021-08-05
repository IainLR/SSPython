import math

# 1
my_diverse_list = ['word', 5, 14.2]
print(my_diverse_list) 

# 2
nested_list = [1,1,[1,2]]
print(nested_list[2][1])

# 3
lst=['a','b','c']
print(lst[1:])

# 4
weekday_dictionary = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
print(weekday_dictionary['Sunday'])

# 5
D={'k1':[1,2,3]}
print(D['k1'][1])

#6
tup_list = [1,[2,3]]
print(tuple(tup_list))

# 7
mississippi_set = set('Mississippi')
print(mississippi_set)

# 8
# yes
mississippi_set.add('X')
print(mississippi_set)

# 9
print(set([1,1,2,3]))

#10
def div_seven_mult_five():
    result_list =[]
    for i in range(2000, 3200):
        if i % 7 == 0 and i % 5 != 0 :
          result_list.append(i)
        else:
          pass
    print(result_list)

# div_seven_mult_five()

# 11
def my_factorial(num):
    print(math.factorial(num))

my_factorial(8)

# 12

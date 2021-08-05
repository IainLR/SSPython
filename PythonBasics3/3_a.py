import random

# 1
def div_seven_mult_five():
    result_list =[]
    for i in range(1500, 2700):
        if i % 7 == 0 and i % 5 != 0 :
          result_list.append(i)
        else:
          pass
    print(result_list)

# div_seven_mult_five() 

# 2
def temp_conversion(celc_or_faren, num):
    if celc_or_faren == 'to Celcius':
        print(round(((num-32)*5)/9))
    elif celc_or_faren == 'to Fahrenheit':
        print(round((1.8*num) + 32))

temp_conversion('to Celcius', 45)
temp_conversion('to Fahrenheit', 60)

# 3
def between_1_and_9():
    our_number = random.randint(1,9)
    loop = True
    while loop:
        response = int(input())
        if response == our_number:
            print("Correct! Well guessed")
            loop = False
        else:
            print("guess again")

# between_1_and_9()

# 4
def pattern_maker(n):
    
    for i in range(n):

        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
    
    for i in range(n+1):

        for j in range(n, i-1, -1):
            print("* ", end="")
        print("\r")


pattern_maker(5) 

# 5
def reverse_your_words():
    response = input()
    print(response[::-1])

# reverse_your_words()

# 6
def even_and_odd_count(num_list):
    odd_count = 0
    even_count = 0
    for num in num_list:
        if num%2==0:
            even_count+=1
        else:
            odd_count+=1
    print("even numbers: " + str(even_count))
    print("odd count: " + str(odd_count))

even_and_odd_count([1,2,3,4,5,6,7,8,9]) 
     
# 7
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

def type_printer(list_of_stuff):
    for item in list_of_stuff:
        print(type(item))

type_printer(datalist)

# 8
def print_with_exceptions(our_range):
    for i in range(our_range):
        if i%3==0 and i !=0:
            continue
        print(i)
     
print_with_exceptions(6)
 
     

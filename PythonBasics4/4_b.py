# 1
book_data = [{'Order Number': 34587, 'Book Title and Author': 'Learning Python, Mark Lutz', 'Quantity': 4, 'Price per Item': 40.95}, {'Order Number': 98762, 'Book Title and Author': 'Programming Python, Mark Lutz', 'Quantity': 5, 'Price per Item': 56.80}, {'Order Number': 77226, 'Book Title and Author': 'Head First Python, Paul Barry', 'Quantity': 3, 'Price per Item': 32.95}, {'Order Number': 88112, 'Book Title and Author': 'Einführung in Python3, Bernd Klein', 'Quantity': 3, 'Price per Item': 24.99}]

def order_number_and_cost(a_list):
    return_list = []
    
    for item in a_list:
        list_to_tuple = []
        temp = list(map(lambda key : item[key],  item))
        list_to_tuple.append(temp[0])
        value = temp[2] * temp[3] if (temp[2] * temp[3]) >= 100 else temp[2] * temp[3] + 10
        list_to_tuple.append(round(value, 2))
        
        return_list.append(tuple(list_to_tuple))
    return return_list
      
print(order_number_and_cost(book_data))  

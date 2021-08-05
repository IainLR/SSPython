# 1
list_of_names = ['doug', 'Cyrano', 'Debbie']

def crowd_test(list):
    if len(list_of_names) > 2:
        print('This room is crouded')

crowd_test(list_of_names)

list_of_names.remove('doug')

crowd_test(list_of_names)

# 2
list_of_names = ['doug', 'Cyrano', 'Debbie']

def crowd_test_2(list):
    if len(list_of_names) > 2:
        print('This room is crouded')
    else:
        print('This room is not particularly crouded')

crowd_test_2(list_of_names)

list_of_names.remove('doug')

crowd_test_2(list_of_names)

# 3
list_of_names = ['doug', 'Cyrano', 'Debbie', 'Rachel', 'Vince', 'charles']

def crowd_test_3(list):
    if len(list_of_names) > 5:
        print('There is a mob in this room')
    elif len(list_of_names) > 2:
        print('This room is crouded')
    elif len(list_of_names) > 0:
        print('This room is not particularly crouded')
    else:
        print('The room is empty')

crowd_test_3(list_of_names)

list_of_names.remove('doug')

crowd_test_3(list_of_names) 
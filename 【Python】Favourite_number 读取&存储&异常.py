import json

def stored_num():
    filename = 'get_number.json'
    try:
        with open(filename) as num:
            the_number = json.load(num)
    except FileNotFoundError:
        return None
    else:
        return the_number


def get_num():
    the_number = input("What's your favourite number? ")
    filename = 'get_number.json'
    with open(filename, 'w') as num:
        json.dump(the_number, num)
    return the_number

def show_num():
    the_number = stored_num()
    if the_number:
        print("I know your favorite number! It's " + str(the_number) + '.')
    else:
        the_number = get_num()
        print("We'll remember your number! ")

show_num()
import json

def stored_name():
    filename = 'username.json'
    try:
        with open(filename) as name_file:
            name = json.load(name_file)
    except FileNotFoundError:
        return None
    else:
        return name

def get_name():
    filename = 'username.json'
    name = input("What's your name? ")
    with open(filename, 'w') as name_file:
        json.dump(name, name_file)
    return name

def show_name():
    name = stored_name()
    if name:
        judge = input("Are you " + name + '?(y/n)')

        if judge == 'y':
            print("Welcome back, " + name + '.')

        else:
            name = get_name()
            print("We'll remember you when you come back, " + name + '.')

    else:
        name = get_name()
        print("We'll remember you when you come back, " + name + '.')

show_name()


#user_info
def build_profile(first, last, **user_info):
    profile = {}
    profile['First name'] = first.title()
    profile['Last name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)

#Enter one's name
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
Judge = True
while Judge:
    print("\nPlease tell me your name: ")
    print("You can press 'q' to quit")
    f_name = input("\tFirst name: ")
    if f_name == 'q':
        break
    l_name = input("\tLast name: ")

    if l_name == 'q':
        break
    real_name = get_formatted_name(f_name, l_name)
    print("\nHello! " + real_name + '!')
    print("Do you want to continue? (yes/no)")
    Judge = input()
    if Judge == 'no':
        Judge = False

#City&Country
def city_country(city, country):
    city_plus_country = city + ', ' + country
    return city_plus_country.title()

print("\nPlease enter the city & country:")
city = input("\tCity: ")
country = input("\tCountry: ")
print(city_country(city, country))

file_path = r'C:\Users\yl601\Desktop\python_code\pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
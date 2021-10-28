import re

numbers_list = ['9999999999', '999999-999', '99999x9999', '899999-999', '8999999999']

example_good_number = r'\b[9,8]{1}\d{9}'

for number in numbers_list:
    x = re.fullmatch(example_good_number, number)
    if x:
        print(f"{numbers_list.index(number) + 1}: всё в порядке")
    else:
        print(f"{numbers_list.index(number) + 1}: не подходит")
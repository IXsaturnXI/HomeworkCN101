#6810742681 เศรษฐการ มณีสวัสดิ์
#Single parameter (1) pages 43
print('-----Single parameter (1) pages 43-----')
def print_digit(a_string):
    all_digits = '0123456789'
    lst = []
    for char in a_string:
        if char in all_digits:
            lst.append(char)
    print(' '.join(lst))
print_digit('24 hours in 1 day, 7 days in a 1 week.')
massage = 'I met a man with 7 wives. Each wife had 7 sacks.'
print_digit(massage)

#Single parameter (2) pages 44
print('-----Single parameter (2) pages 44-----')
def print_even(a_list):
    even_numbers = []
    for number in a_list:
        if number % 2 == 0:
            even_numbers.append(str(number))
    print(' '.join(even_numbers))
print_even([1,2,3,4,5])
list_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 20, 21, 20]
list_2 = list(range(20, 0, -3))
print_even(list_1)
print_even(list_2)




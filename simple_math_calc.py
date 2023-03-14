#Addition, Subtraction, Multiplication, and Division calculator 
num_a = input('Enter a number> ')
num_b = input('Enter another number> ')
value_1 = int(num_a)
value_2 = int(num_b)
number_list = []
number_list.append(value_1)
number_list.append(value_2)

print(f'What would you like to do with these numbers: {value_1} and {value_2}')

math_list = ['add', 'subtract', 'multiply', 'divide']
for math in math_list:
     print('-', math)

add = math_list[0]
subtract = math_list[1]
multiply = math_list[2]
divide = math_list[3]

first_num = number_list[0]
second_num = number_list[1]

conversion_add = sum(number_list)
conversion_sub = first_num - second_num
conversion_mult = first_num * second_num
conversion_div = first_num // second_num


dec = input('Enter your choice> ')     
       
if dec == add:
   print(f'Your answer is: {conversion_add}')
elif dec == subtract:
     print(f'Your answer is: {conversion_sub}')
elif dec == multiply:
     print(f'Your answer is: {conversion_mult}')
elif dec == divide:
     print(f'Your answer is: {conversion_div}')
else:
    print('That is not a choice.')
     

    
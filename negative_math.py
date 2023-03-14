#Solving negative equations
num_a = input('Enter a number> ')
num_b = input('Enter another number> ')
value_1 = int(num_a)
value_2 = int(num_b)


sample_tump = ('-a-b', 'a-(-b)','-a-(-b)', 'a-b')
for sample in sample_tump:
    print(f'Sample Equations: {sample}')

inp = input('Choose an equation> ')
if inp == sample_tump[0]:
    equation_1 = -value_1-value_2
    print(f"The answer is: {equation_1}")
elif inp == sample_tump[1]:
    equation_2  = value_1-(-value_2)
    print(f"The answer is: {equation_2}")
elif inp == sample_tump[2]:
    eqaution_3 = -value_1-(-value_2)
    print(f"The answer is: {eqaution_3}")
elif inp == sample_tump[3]:
    equation_4 = value_1-value_2
    print(f"The answer is: {equation_4}")
else:
    print('That is not a choice.')


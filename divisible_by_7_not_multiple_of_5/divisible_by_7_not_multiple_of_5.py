
'''Write a program which will find all such numbers that are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included). The numbers should be printed on the output screen.
(Bonus point if you can print all the numbers on a single line)'''
numbers = [x for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0]
def new_func(numbers):
    new_varnew_var = print(','.join(map(str, numbers)))

new_func(numbers)

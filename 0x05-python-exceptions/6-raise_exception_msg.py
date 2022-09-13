#!/usr/bin/python3
def safe_print_list(my_list=[], x=0 ):
    count = 0
    while count < x:
        try:
            print(next(my_list))
        except StopIteration:
            print("You have reached the end!")
            break
        count += 1
            
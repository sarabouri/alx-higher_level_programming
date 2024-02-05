#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    set = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end="")
                    set += 1
        except IndexError:
            break
        print("")
        return (set)

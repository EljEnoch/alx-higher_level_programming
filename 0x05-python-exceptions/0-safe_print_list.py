#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nbprint = 0
    for ele in my_list[:x]:
        try:
            nbprint += 1
            print(ele, end="")
        except IndexError:
            break
        print("")
        return nbprint

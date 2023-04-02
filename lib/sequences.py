#!/usr/bin/env python3

def print_fibonacci(length):
    array = []
    if length > 0:
        array.append(0)
        if length > 1:
            array.append(1)
            if length > 2:
                for i in range(2,length):
                    array.append(array[i-1] + array[i-2])


    
    
    return array

print(print_fibonacci(9))
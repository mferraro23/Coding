if __name__ == '__main__':
    n = int(input()) #handle unnecessary input 
    arr = map(int, input().split()) #grab all inputs
    arr = set(arr) #turning to a set which removes all extra instances of the same element 
    arr = list(arr) #turning to a list so it can be sorted
    print(arr)
    arr = sorted(arr) #making the list sorted 
    print(arr[-2]) #finds second biggest value in sorted list
    print(sorted(list(set(arr)))[-2])

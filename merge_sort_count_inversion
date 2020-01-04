import math
inversion = 0

def merge_sort(arr):
    global inversion
    length_a = len(arr)
    if length_a == 1:
        return arr
    elif length_a == 2:
        if arr[0] > arr[1]:
            inversion += 1
            return [arr[1],arr[0]]
        else:
            return arr
    else:
        half_size = math.floor(length_a/2)
        #print(f"The left_half is {arr[:half_size]}")
        #print(f"The right_half is {arr[half_size:]}")
        left_array = merge_sort(arr[:half_size])
        #print(f"The current left_array is {left_array}")
        right_array = merge_sort(arr[half_size:])
        #print(f"The current right_array is {right_array}")
        return merge(left_array,right_array)
        

def merge(l,r):
    global inversion
    length_l = len(l)
    length_r = len(r)
    new_array = [0] * (length_l + length_r)
    #print(f"The merge function is triggered and the current left is {l} and right is {r}")
    i = 0
    j = 0
    k = 0
    while i != length_l and j != length_r:
        if l[i] < r[j]:
            new_array[k] = l[i]
            #print(new_array)
            i += 1
        else:
            #print(f"AL: Inversion found {l[i]} and {r[j]}")
            new_array[k] = r[j]
            inversion += length_l - i
            #print(new_array)
            j += 1
        k += 1
    if i == length_l: #append what's left in the right part
        while j != length_r:
            new_array[k] = r[j]
            #print(new_array)
            j += 1
            k += 1
            
    else: #append what's left in the left part
        while i != length_l:
            new_array[k] = l[i]
            #print(new_array)
            i += 1
            k += 1
            
    #print(f"the merged new array is {new_array}")
    #print(f"{inversion} inversion found")
    return new_array

def complex_inversion(a): #this is to check the correctness of the number of inversions, using naive algorithm
    reversion = 0
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i] > a[j]:
                #print(f"Na: Inversion found, {a[i]} and {a[j]}")
                reversion += 1
    return reversion
                
                


def main():
    global inversion

    #uncomment the following codes to read data from a text
    #with open("test_merge_sort_array.txt", 'r') as file:
    #with open("test.txt", 'r') as file:
    #    for line in file:
    #        original_array.append(int(line))
        
    original_array = [1,2,4,6,7,5,3,9]
    
    
    print(f"The original array is {original_array}");
    
    #sort array
    sorted_array = merge_sort(original_array)
    print(f"The sorted array is {sorted_array}");
    
    #count inversion
    print(f"There are {inversion} inversions found")
    naive = complex_inversion(original_array)
    print(f"CHECK, usint the naive algorithm, inversion is {naive}")


if __name__ == '__main__':
    main()


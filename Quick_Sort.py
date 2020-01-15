
###########################  global variables declaration##########################################
import math
import time
comparison = 0
###########################  initialization and helper##########################################
def read_file(f_name):
    num_list = []
    with open(f_name) as file:
        for line in file.readlines():
            #print(line)
            num_list.append(int(line[:-1]))
    file.close()
    #print(len(num_list))
    return num_list

def get_median(l, low, high): #notice, all the first/last/median variables refer to the value of the corresponding index
   
    #print(f"Func get_median, input l is {l} and the low is {low} while the high is {high}, the list is in fact {l[low:high+1]}")
    length = high-low+1

    
    first = l[low]
    last = l[high]

    if length == 2:
        if first > last:
            return high
        else:
            return low
    

    #get the median index
    index_mid = math.floor(length/2) + low
   
    if length % 2 == 0:
        index_mid = index_mid -1
        median = l[index_mid]
    else:
        median = l[index_mid]

   
    temp_dic = {first: low, last: high, median: index_mid}
    #print(temp_dic)
    
    max_num = max(temp_dic)
    del temp_dic[max_num]
    min_num = min(temp_dic)
    del temp_dic[min_num]
    #print(f"in Func get_median, return {temp[0]}")
   
    for k in temp_dic:
        #print(f"For the three numbers first {l[low]}, median {l[index_mid]} and last {l[high]}, the median number is {k} and the corresponding index is {temp_dic[k]}")
        return temp_dic[k]#return the index of the median number
###########################  partition function  ##########################################################
def partition(l, low, high):
    #if low < high:
    global comparison
    comparison += high - low 
    p = l[low]
    i = low + 1
    j = i
    #print(f"START l is {l}, low is {low}, high is {high}, p is {p}")
    while j <= high:
        
        if l[j] < p:
            buff = l[j]
            l[j] = l[i]
            l[i] = buff
            i += 1 #so eveyrthing on the left side of i is smaller or equal to p
        j += 1
                
        #sawp the pivot and the rightest smallest item
    buff = l[low]
    l[low] = l[i-1]
    l[i-1] = buff
    #print(f"END: l is {l}, return value is {i-1}")
        
    return i-1




###########################  sorting function  ##########################################################

def quick_sort_first(l, low, high):
    if low < high:
        j = partition(l, low, high)
        quick_sort_first(l, low, j-1)
        quick_sort_first(l, j+1, high)
        return l
def quick_sort_median(l, low, high):
    if low < high:
        #swap the median and the first
        #print(f"Before swap the ls is {l}")
        median_index = get_median(l, low, high)
        if median_index != low:
            buff = l[median_index]
            l[median_index] = l[low]
            l[low] = buff
        #print(f"After swap the ls is {l}")
        j = partition(l, low, high)
        quick_sort_median(l, low, j-1)
        quick_sort_median(l, j+1, high)
        return l
    
def quick_sort_last(l, low, high):
    if low < high:
        #swap the first and the last item
        buff = l[low]
        l[low] = l[high]
        l[high] = buff
        j = partition(l, low, high)
        quick_sort_last(l, low, j-1)
        quick_sort_last(l, j+1, high)
        return l


###########################  main function  ##########################################################
def choose(mode, original_list):
   
    global comparison

    buff_list = original_list
    start = time.time()
    if mode == 1: #first digit is chosen as the pivot
        sorted_list = quick_sort_first(original_list,0, len(original_list)-1)
        
    elif mode == 2: #median as the pivot
        sorted_list = quick_sort_median(original_list,0, len(original_list)-1)
        
    else:
        sorted_list = quick_sort_last(original_list, 0, len(original_list) -1)
       
    finish = time.time()
    pivod_dic = {1: "choose the FIRST as pivot", 2:"choose the Median as pivot", 3:"choose the LAST as pivot"}

    print(f"The total comparison time in mode {pivod_dic[mode]} is {comparison}. The sorting takes {finish-start} seconds.")
    comparison = 0
    
def main(original_list): #takes original list 
    global comparison
    buff_list = original_list.copy()
    
    #pivod choosing mode 1 2 3, see more details in choose function
    for mode in range(1,4):
        choose(mode, original_list)
        original_list = buff_list.copy()
       
        
       
    #choose(1,original_list)
    #choose(2,original_list)
    #choose(3,original_list)
    
   
    ############################compare the comparison times###############################################
  

if __name__ == '__main__':
    original_list = read_file("my_qs_test.txt")
    #original_list = read_file("QuickSort.txt")
    #original_list = read_file("qs.txt")
    #print(original_list)
    main(original_list)

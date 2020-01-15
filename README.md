# algorithms_implementation
This repository includes implementations of various kinds of algorithms in PYTHON3

- ## 1. **Merge Sort** 
  - 1.1 Algorithm: merge sort.
  - 1.2 Complexity: O(nlogn)
  - 1.3 Function: the scripts can count the inversions of a given array, in which no repetitive numbers is guaranteed.
    - 1.3.1 Given Array info:
    - 1.3.1.1 Random, non-repeated number between (1,10000)
    -  1.3.1.2 Size: 9999
  - 1.4 Focus: Master Method
  
- ## 2. **Quick Sort** 
  - 2.1 Algorith: quick sort
  - 2.2 Complexity: O(nlogn)
  - 2.3 Function: the scripts can count the times of comparing pivot and other elements in a given array. (this comparison dominates the complexity)
    - 2.3.1 Given Array info: 
    - 2.3.1.1 Random, non-repeated number between (1,100000)
    - 2.3.1.2 Size: 99999
  - 2.4 Analysis: 
    - 2.4.1 choice of pivot matters significantly to how the algorithms performs. This script implemented three ways of choosing pivot.
      - 2.4.1.1 Always choose the first element as the pivot. (Notice: first means index)
      - 2.4.1.2 Always choose the median element as the pivot. (IMPORTANT Notice: median means the value not index)
      - 2.4.1.3 Always choose the last element as the pivot. (Notice: last means index)
      - 2.4.1.4 For example, if a given array L is [2,4,6,1]. 
        - **FIRST_CHOICE**: The first choice is to use the L[0] as the pivot (value is 2). We use 2 to compare with 4, 6, 1. 
        - **MEDIAN_CHOICE**: The second choice is to use the L[1] as the pivot (value is 4). Among the three values L[0], l[3] and L[1], we have set {2,4,1}, the median is the value 2. So, we use 2 to compare with 2, 4, 6. 
        - **LAST_CHOICE**: The last choice is to use L[3] as the pivot (value is 1). We use 1 to compare with 2, 4 and 6.
     - 2.4.2 Performance. 
      - 2.4.2.1 Input Array size: 99999
      - 2.4.2.2 Evaluation:
        - The First_element_as_pivot choice is as good as the Last_element_as_pivot choice. The Median_element_as_pivot performs the best. 
      - 2.4.2.3 Results:
        - The total comparison time in mode choose the FIRST as pivot is 1932190. The sorting takes 0.31453680992126465 seconds.
        - The total comparison time in mode choose the Median as pivot is 1666172. The sorting takes 0.3374748229980469 seconds.
        - The total comparison time in mode choose the LAST as pivot is 1991625. The sorting takes 0.33668088912963867 seconds.
      - 2.4.2.4 Interesting Observation:
       - 2.4.2.4.1 Why does the first method costs the least time?
          Though the second choice (Median_as_pivot) leads to the smallest comparison times, the first choice (First_as_pivot) actually costs the least time. This is caused by the fact that both the median and last take an extra step to swap the chosen pivot and the first element in a given array. 
       - 2.4.2.4.2 Why does the second and the third method cost similar time? 
          The Median_as_pivot_method not only have an extra step to swap the chosen pivot and the first element, it also takes an extra step to choose the median value from a given array. The fact that it uses the same amount of time as the third method exactly proves that it performs better in sorting despite that it has an extra step.
       - 2.4.2.4.3 Optimization: focus can be put on optimizing the find_median helper function.
        
      
    
  

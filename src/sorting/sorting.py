# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    
    res =[] #this will be the final array
    # index for left and right array and for final array
    left = 0
    right = 0
    

    #this will run while the index is less than the array
        #if value A is less than value B add to final array
        #
    while left < len(arrA) and right < len(arrB):
        if arrA[left] < arrB[right]:
            res.append(arrA[left])
            left += 1
        else:
            res.append(arrB[right])
            right += 1
    
    while left < len(arrA):
        res.append(arrA[left])
        left += 1
    
    while right < len(arrB):
        res.append(arrB[right])
        right += 1


    return res

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2: ])
        arr = merge(left, right)
     

    


    return arr

# test = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# merge_sort(test)

print(merge_sort([85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]))
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len( arrA ) + len( arrB )
    # This below is used to intialize an empty array
    merged_arr = []
    # We will establish the first index value for the A partition and B partition
    # TO-DO
    left = 0
    right = 0
    # This will end the loop when the length of each partition A and B has been reached
    while left < len(arrA) and right < len(arrB):
        # Compare the value of the left index value to the right index value in each partition
        # If left value is less then append that value to the array A partition and increment to next
        # left value with +=1, do the same with the right value
        if arrA[left] < arrB[right]:
            merged_arr.append(arrA[left])
            left += 1
    while right < len(arrB):
        merged_arr.append(arrB[right])
        right += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # Establish the base case of array length smaller than 1 where merge_sort will end
    if len(arr) <= 1
    return arr

   # Create a middle point to split the array up and use // to floor divide down to an appropriate
   # index value
   split_array= len(arr) //2
   # establish reference for left and right side of array and recursively call merge_sort function
   # pass in values from beginning of array to the index split point and from the index split point to the end of the array on the right side
    left_side= merge_sort(arr[:split_array])
    right_side = merge_sort(arr[split_array:])
    # return by calling merge function within merge_sort and join left and right side
    return(merge(left_side, right_side))

# test with print by passing in a list of values
print(merge_sort([99, 32, 86, 54, 33, 11111, 2, 8, 99, 103]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

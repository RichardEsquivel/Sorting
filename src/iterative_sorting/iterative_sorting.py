
# ### Algorithm
# 1. Start with current index = 0

# 2. For all indices EXCEPT the last index:

#     a. Loop through elements on right-hand-side
#     of current index and find the smallest element

#     b. Swap the element at current index with the
#     smallest element found in above loop


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i  # set default  value of index for comparison with smallest_index
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # starts from current index to end of array
        for elem in range(i+1, len(arr)):
            # from elements above current element if value above is less than current index
            # set the current index of smallest index equal to that index value
            if arr[elem] < arr[smallest_index]:
                smallest_index = elem
        # TO-DO: swap
            # perform swap assignment of values at these two indexes using swap syntax
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    x = True
    while x:
        x = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                x = True
    return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr


print(selection_sort([85, 22, 89, 101, 7, 4]))
print(bubble_sort([85, 22, 89, 101, 7, 4]))

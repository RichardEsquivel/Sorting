
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
        for j in range(i+1, len(arr)):
            # from elements above current element if value above is less than current index
            # set the current index of smallest index equal to that index value
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
            # perform swap assignment of values at these two indexes using swap syntax
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    '''Will assume True for swapped state as the
      array being passed in is going to have swapped action performed on it.'''
    swapped = True
    while swapped:
    '''This swapped above will only = false will and break the loop once the
       if statement where left value is not greater than the right value is not true
       and will then make statement false and break the loop'''
     swapped = False
      for i in range(0, len(arr) - 1):
           if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
            swapped = True
    return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr


print(selection_sort([85, 22, 89, 101, 7, 4]))
print(bubble_sort([85, 22, 89, 101, 7, 4]))

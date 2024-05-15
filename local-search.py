import random
from itertools import combinations
def search(dct):
    # YOUR CODE HERE. Do not change the name of the function.
    """returns a list of subsets of equal sums"""
    # iniitialize variables
    count = dct["count"]
    size = dct["size"]
    values = dct["values"]
    target_sum = sum(values) // count # sum for each subset
    
    # checks if dividing values is possible
    if len(values) != count * size:
        return None
        
    subsets = initialize_subsets(values, count, size)
    while True:
        # find swap that brings us cloer to target sum for each of the subsets
        swap = find_swap(subsets, target_sum)
        if not swap:
            # no swap found, so do a random restart
            random.shuffle(values)
            subsets = initialize_subsets(values, count, size)
            continue
        # apply the swap that was found by find_swap()
        max_index, min_index, max_val, min_val = swap
        subsets[max_index].remove(max_val)
        subsets[min_index].remove(min_val)
        subsets[max_index].append(min_val)
        subsets[min_index].append(max_val)
        
        # check if all subsets have the same sum
        if all(sum(subset) == target_sum for subset in subsets):
            return subsets
        
def initialize_subsets(values, count, size):
    """returns a list of subsets"""
    subsets = []
    for i in range(0, len(values), size):
        subset = values[i:i + size] # create subsets starting from index i to "size" number of elements
        subsets.append(subset) # add subsets to a list of subsets
    return subsets
        
def find_subset_sums(subsets):
    """returns a list of sums for each of the subsets in the list of subsets"""
    sums = []
    for subset in subsets:
        subset_sum = sum(subset) # calculate sum
        sums.append(subset_sum) # add sum to a list of sums
    return sums
def find_swap(subsets, target_sum):
    """finds a potential swap between two subsets to bring them closer to a target sum and returns this swap in the form of a tuple"""
    
    subset_sums = find_subset_sums(subsets) # calculate sums for each subset
    
    max_index = subset_sums.index(max(subset_sums)) # index of subset with maximum sum
    min_index = subset_sums.index(min(subset_sums)) # index of subset with minimum sum
    
    # loop through each of the values in each subset to find a pair of values that would bring the sum of both subsets closer to the target sum
    for i in subsets[max_index]:
        for j in subsets[min_index]:
            # calculate the new sums if the swap was applied
            max_sum = sum(subsets[max_index]) - i + j
            min_sum = sum(subsets[min_index]) + i - j
            # check if the swap is beneficial by checking the sums of the max and min subsets against the target sum
            if abs(max_sum - target_sum) < abs(subset_sums[max_index] - target_sum) and abs(min_sum - target_sum) < abs(subset_sums[min_index] - target_sum):
                return max_index, min_index, i, j
    
    return None
import time
import random

def interpolation_search(arr, target):
    """
    Performs an interpolation search on a sorted, uniformly distributed array.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        # Interpolation formula to estimate probe position
        # Using integer division to replicate the FLOOR logic safely
        pos = low + int(((target - arr[low]) * (high - low)) // (arr[high] - arr[low]))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
            
    return -1

def binary_search(arr, target):
    """
    Performs a standard binary search on a sorted array.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

# --- Benchmarking Script ---
if __name__ == "__main__":
    dataset_sizes = [1000, 5000, 10000, 50000, 100000]
    
    print(f"{'Dataset Size':<15}{'Binary Search (s)':<22}{'Interpolation Search (s)':<25}")
    print("-" * 62)
    
    for size in dataset_sizes:
        # Generate a uniformly distributed sorted array
        arr = [i * 3 for i in range(size)]
        
        # Pick a target element present in the array to evaluate search depth
        target = arr[int(size * 0.75)]
        
        # Benchmark Binary Search
        start_time = time.perf_counter()
        binary_search(arr, target)
        end_time = time.perf_counter()
        bin_time = end_time - start_time
        
        # Benchmark Interpolation Search
        start_time = time.perf_counter()
        interpolation_search(arr, target)
        end_time = time.perf_counter()
        interp_time = end_time - start_time
        
        print(f"{size:<15}{bin_time:<22.8f}{interp_time:<25.8f}")   
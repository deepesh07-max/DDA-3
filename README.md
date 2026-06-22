Program (Python)
This script implements both search strategies alongside an automated benchmarking routine that generates a uniformly distributed array of items to cleanly evaluate performance differences.
# Interpolation Search vs. Binary Search Analysis

**Subject:** CS5303 - Design and Analysis of Algorithms  
**Experiment No:** 1  

---

## Problem Statement
Given a sorted array of uniformly distributed integers, implement **Interpolation Search** to find the position of a target element. Compare its performance with **Binary Search** for different dataset sizes (1,000, 5,000, 10,000, 50,000, and 100,000 elements).

## Aim
To implement the Interpolation Search algorithm in Python and analyze its time complexity by measuring execution time on sorted datasets of varying sizes.

---

## Pseudocode

```text
INTERPOLATION_SEARCH(arr, target):
    low ← 0
    high ← len(arr) - 1
    
    WHILE low ≤ high AND target ≥ arr[low] AND target ≤ arr[high]:
        IF low = high:
            IF arr[low] = target: 
                RETURN low
            ELSE: 
                RETURN -1
        
        // Interpolation formula to estimate probe position
        pos ← low + ((target - arr[low]) * (high - low)) / (arr[high] - arr[low])
        pos ← FLOOR(pos)
        
        IF arr[pos] = target:
            RETURN pos
        ELIF arr[pos] < target:
            low ← pos + 1
        ELSE:
            high ← pos - 1
            
    RETURN -1 // Element not found

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary search to find the position where x fits or the closest element
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid

        left, right = l - 1, l  # Start pointers where binary search ended

        result = []
        while len(result) < k:
            # If left pointer is out of bounds, take from right
            if left < 0:
                result.append(arr[right])
                right += 1
            # If right pointer is out of bounds, take from left
            elif right >= len(arr):
                result.append(arr[left])
                left -= 1
            else:
                # Compare distances to x
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    result.append(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1

        return sorted(result)  # sort to maintain order

# Leetcode solutions written for club
# The problem number is above each function

from collections import defaultdict
from math import sqrt
class Solution:
    #1
    # one pass solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i, v in enumerate(nums):
            t = target - nums[i]
            if t in x:
                return [x[t], i]
            x[nums[i]] = i


    # 1365
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # We know we have a fixed n=100 possible numbers in the list
        # Bucket sort allows us to complete this problem in O(n) time, with essentially constant space complexity
    
        c_arr = [0] * 102
        for i in nums:
            c_arr[i+1] += 1     # Incrementing the number of numbers less than the current number + 1 
        
        # Now, for each number in the list, we can add up count of the numbers less than that number to output a result
        for i in range(1, 102):
            c_arr[i] += c_arr[i-1]
        return [c_arr[i] for i in nums]

    # 1512
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # O(n) solution
        d = {}  # could use defaultdict here
        ans = 0
        for number in nums:
            if number in d.keys():
                d[number] += 1
            else:
                d[number] = 0
        for counted in d.values():
            ans += (counted(counted+1))/2
        return int(ans)


    # 973
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # Nice one liner, but it is N LOG N
        # Divide and conquer solution would be N best case, N^2 worst case
        return sorted(points, key=lambda coord: sqrt((coord[0]**2)+(coord[1]**2)))[0:K]


    # 139
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        false_statements = set()
        def recurs(start):
            if start in false_statements:
                return False
            if start == len(s):
                return True
            for w in wordDict:
                if start+len(w) <= len(s) and s[start:start+len(w)] == w:
                    if recurs(start + len(w)):
                        return True
            else:
                false_statements.add(start)
                return False
        return recurs(0)


    # 4   --> THIS SOLUTION IS A VARIANT SPECIFICALLY FOR A PROBLEM GIVEN IN CLASS
    #          Given two sets of equal size n, with the ability to query the K'th largest element of each set, what is the median of the two sets?
    def findMedianSortedArrays(self, A, B, n) -> float:
        # THIS IS A CLEAN O(LOGN) solution, with O(LOGN) queries
        l, r = 0, n
        while l <= r:
            s1 = (l + r) / 2
            s2 = n - s1
            if s1 < n and queryB(n-(s2-1)) > queryA(n-s1):    l = s1 + 1
            elif s1 > 0 and queryA(n-(s1-1)) > queryB(n-s2):  r = s1 - 1
            else:
                if s1 == 0: lmax = queryB(n-(s2-1))
                elif s2 == 0: lmax = queryA(n-(s1-1))
                else: lmax = max(queryA(n-(s1-1)), queryB(n-(s2-1)))

                if s1 == n: rmin = queryB(n-s2)
                elif s2 == n: rmin = queryA(n-s1)
                else: rmin = min(queryA(n-s1), queryB(n-s2))

        return (lmax + rmin)/2
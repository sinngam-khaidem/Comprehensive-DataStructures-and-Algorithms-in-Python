from typing import List

class ArraySolution:
    # Valid Anagram
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = {}
        for i in range(len(s)):
            hm[s[i]] = hm.get(s[i], 0) + 1
            hm[t[i]] = hm.get(t[i], 0) - 1
        for j in hm.values():
            if j != 0:
                return False
        return True

    # Maximum Subarray using Kadane's algorithm
    def maxSubarray(self, nums) -> int:
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            if curSum <0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum
    
    # Majority element 1
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1

        for key, val in hm.items():
            if val > len(nums)//2:
                return key
        return 0

    # Majority element 2
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        
        majors = [key for key, val in hm.items() if val > len(nums)//3]
        return majors

    # Group anagrams 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in hm.keys():
                hm[s_sorted].append(s)
            else:
                hm[s_sorted] = [s]
        return hm.values()
    
    # Top K Frequent elements - Sorting approach O(nlogn)
    # Using a heap could reduce time to O(klogn)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1

        mappings = [(key, val) for key, val in hm.items()]
        mappings.sort(key=lambda x: x[1], reverse=True)
        
        result = []
        for i in range(k):
            result.append(mappings[i][0])
        return result
    
    # Top K Frequent elements - Bucket Sort approach O(k+n) ~ O(n)
    # https://www.youtube.com/watch?v=YPTqKIgVk-k&t=22s
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    # Longest Consecutive Sequence
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        curCount = 1
        maxCount = 1
        prev = nums[0] 
        for n in nums:
            if n - 1 == prev:
                curCount += 1
            elif n - 1 > prev:
                curCount = 1
            maxCount = max(curCount, maxCount)
            prev = n
        return maxCount

print(ArraySolution().topKFrequent([1,1,1,2,2,3], 3))